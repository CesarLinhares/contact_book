from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from src.core.interfaces.repository.user_data.interface import IUserData
from src.infra.mongo_connection import MongoConnection


class RepositoryMongo(IUserData):
    connection_infra = MongoConnection()
    connection: MongoClient = connection_infra.get_connection()
    database: Database = connection.contact_book
    collection: Collection = database.contacts

    def delete(self, _id: str) -> bool:
        deleted = self.collection.delete_one({'_id': _id})
        return bool(int(deleted.deleted_count))

    def register_a_contact(self, item: dict) -> bool:
        return bool(self.collection.insert_one(item))

    def update_a_contact(self, _id: str, item: dict) -> bool:
        update = self.collection.update_one({'_id': _id}, {'$set': item})
        return bool(int(update.modified_count))

    def find_one_contact(self, _id: str) -> dict:
        return self.collection.find_one({'_id': _id, 'active': True})

    def find_all_contacts(self) -> list:
        return list(self.collection.find({'active': True}))

    def find_contacts_by_letter(self, letter: str) -> list:
        return list(self.collection.find({"firstName": {"$regex": f"^[{letter.upper()}{letter.lower()}]"}, 'active': True}))
