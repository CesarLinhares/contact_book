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
        '''
        _id
        firstName
        lastName
        email
        phoneList
        address
        active

        '''
        print(item)

        def _insert_phones(phone_list: List[dict]) -> str:
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

        sql_contacts = f'''
        INSERT INTO contacts VALUES
        ('{item.get('_id')}', '{item.get('firstName')}', '{item.get('lastName')}', '{item.get('email')}', '{item.get('address')}', 
        {_insert_phones(item.get('phoneList'))}, '{self._register_status.get(item.get('active'))}')
        '''
        try:
            self.cursor.execute(sql_contacts)
            self.connection.commit()
            return True
        except:
            return False

    def update(self, _id: str, item: dict) -> bool:
        update = self.collection.update_one({'_id': _id}, {'$set': item})
        return bool(int(update.modified_count))

    def find_one(self, _id: str) -> dict:
        return self.collection.find_one({'_id': _id, 'active': True})

    def find_all(self) -> list:
        return list(self.collection.find({'active': True}))

    def find_by_letter(self, letter: str) -> list:
        return list(self.collection.find({"firstName": {"$regex": f"^[{letter.upper()}{letter.lower()}]"}, 'active': True}))
