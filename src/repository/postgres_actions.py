from typing import List

import psycopg2

from src.core.enumerator.contact_status import ContactStatus
from src.core.interfaces.repository.postgres.interface import IPostgres
from src.infra.postgres_connection import PostgresConnection


class RepositoryPostgres(IPostgres):
    connection_infra = PostgresConnection()
    connection: psycopg2.connect = connection_infra.get_connection()
    cursor = connection.cursor()

    @staticmethod
    def _transform_row_to_dict(contact: tuple) -> dict:
        phone_list = []
        for phone in range(5, 11, 2):
            if contact[phone] is not None:
                phone_list.append({'number': contact[phone], 'type': contact[phone + 1]})

        contact_dict = {
            "_id": contact[0],
            "firstName": contact[1],
            "lastName": contact[2],
            "email": contact[3],
            "address": contact[4],
            "phoneList": phone_list,
            "active": contact[11]
        }

        return contact_dict

    @staticmethod
    def _insert_phones_str(phone_list: List[dict]) -> str:
        insert_str = ''
        counter = 1

        for phone in phone_list:
            insert = f"\'{phone.get('number')}\', \'{phone.get('type')}\'"
            if counter < len(phone_list):
                insert_str += insert + ', '
            else:
                insert_str += insert

            counter += 1

        return insert_str

    @staticmethod
    def _insert_phone_fields_str(phone_list: List[dict]) -> str:
        phone_fields_str = ''
        counter = 1
        for _ in phone_list:
            insert = f"phone{counter}, phone{counter}_type,"
            phone_fields_str += insert
            counter += 1
        all_fields = f"_id, firstname, lastname, email, address, {phone_fields_str} active"

        return all_fields

    @staticmethod
    def _insert_updates_str(updates_dict: dict) -> str:
        insert_str = ''
        counter = 1

        for key, value in updates_dict.items():
            if key == 'phoneList':
                counter_phone = 1
                phones_str = ''
                for phone in value:
                    insert = f"phone{counter_phone} = \'{phone.get('number')}\', phone{counter_phone}_type = \'{phone.get('type')}\'"
                    if counter < len(value):
                        phones_str += insert + ', '
                    else:
                        phones_str += insert
                    counter_phone += 1

                insert_str += phones_str
            else:
                insert = f"{key.lower()} = \'{value}\'"
                if counter < len(updates_dict):
                    insert_str += insert + ', '
                else:
                    insert_str += insert

            counter += 1

        return insert_str

    def register(self, item: dict) -> bool:
        sql = f'''
        INSERT INTO contacts
        ({self._insert_phone_fields_str(item.get('phoneList'))})
        VALUES
        ('{item.get('_id')}', '{item.get('firstName')}', '{item.get('lastName')}', '{item.get('email')}', '{item.get('address')}',
        {self._insert_phones_str(item.get('phoneList'))}, '{1}')
        '''

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as error:
            self.connection.rollback()
            print(error.__class__)
            return False

    def update(self, _id: str, updates: dict) -> bool:
        sql = f'''
        UPDATE contacts
        SET {self._insert_updates_str(updates)}
        WHERE _id = '{_id}'
        '''

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as error:
            print(error.__class__)
            return False

    def find_one(self, _id: str):
        sql = f"SELECT * FROM contacts WHERE _id = '{_id}' AND active = '{ContactStatus.ACTIVE.value}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if not result:
            return
        else:
            return self._transform_row_to_dict(result[0])

    def find_all(self) -> list:
        sql = f"SELECT * FROM contacts WHERE active = '{ContactStatus.ACTIVE.value}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if not result:
            return []
        else:
            contacts_list = [self._transform_row_to_dict(row) for row in result]
            return contacts_list

    def find_by_letter(self, letter: str) -> list:
        sql = f"SELECT * FROM contacts WHERE (firstname LIKE '{letter.upper()}%' OR firstname LIKE '{letter.lower()}%') AND active = '{ContactStatus.ACTIVE.value}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if not result:
            return []
        else:
            contacts_list = [self._transform_row_to_dict(row) for row in result]
            return contacts_list
