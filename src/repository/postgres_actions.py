from pymongo import MongoClient
from typing import List
from pymongo.collection import Collection
from pymongo.database import Database
import psycopg2

from src.core.interfaces.repository.mongodb.interface import IPostgres
from src.infra.postgres_connection import PostgresConnection


class RepositoryPostgres(IPostgres):
    connection_infra = PostgresConnection()
    connection: psycopg2.connect = connection_infra.get_connection()
    cursor = connection.cursor()

    _register_status = {
        True: 1,
        False: 0
    }

    def delete(self, _id: str) -> bool:
        pass

    def register(self, item: dict) -> bool:
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
        sql = f'''
        INSERT INTO contacts VALUES
        ('{item.get('_id')}', '{item.get('firstName')}', '{item.get('lastName')}', '{item.get('email')}', '{item.get('address')}', 
        {_insert_phones_str(item.get('phoneList'))}, '{self._register_status.get(item.get('active'))}')
        '''
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except:
            return False

    def update(self, _id: str, updates: dict) -> bool:
        def _insert_updates_str(updates_dict):
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

        sql = f'''
        UPDATE contacts
        SET {_insert_updates_str(updates)}
        WHERE _id = '{_id}'
        '''
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as error:
            print(error.__class__)
            return False



    def find_one(self, _id: str) -> dict:
        return self.collection.find_one({'_id': _id, 'active': True})

    def find_all(self) -> list:
        return list(self.collection.find({'active': True}))

    def find_by_letter(self, letter: str) -> list:
        return list(self.collection.find({"firstName": {"$regex": f"^[{letter.upper()}{letter.lower()}]"}, 'active': True}))
