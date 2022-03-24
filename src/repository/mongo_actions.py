from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from src.core.interfaces_repository import IMongo
from src.infra.mongo_connection import MongoConnection


class RepositoryMongo(IMongo):
    connection_infra = MongoConnection()
    connection: MongoClient = connection_infra.get_connection()
    database: Database = connection.contact_book
    collection: Collection = database.contacts

    def delete(self, _id: str) -> bool:
        deleted = self.collection.delete_one({'_id': _id})
        return bool(int(deleted.deleted_count))

    def register(self, item: dict) -> bool:
        return bool(self.collection.insert_one(item))

    def update(self, _id: str, item: dict) -> bool:
        update = self.collection.update_one({'_id': _id}, {'$set': item})
        return bool(int(update.modified_count))

    def find_one(self, _id: str) -> dict:
        return self.collection.find_one({'_id': _id})

    def find_all(self) -> list:
        return list(self.collection.find({'active': True}))

    def find_by_letter(self, letter: str) -> list:
        return list(self.collection.find({"firstName": {"$regex": f"^{letter}"}}))
