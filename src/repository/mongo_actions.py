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
        return bool(self.collection.delete_one({'_id': _id}))

    def register(self, item: dict) -> bool:
        return bool(self.collection.insert_one(item))

    def update(self, _id: str, item: dict) -> bool:
        return bool(self.collection.update_one({'_id': _id}, item))

    def find_one(self, _id: str) -> dict:
        return self.collection.find_one({'_id': _id})

    def find_all(self) -> list:
        return self.collection.find()

    def find_by_letter(self, letter: str) -> list:
        return self.collection.find({})     # TODO: Fazer filtro de busca por letra
