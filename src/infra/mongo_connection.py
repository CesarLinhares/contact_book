from pymongo import MongoClient
from src.infra.connection_links import user


class MongoConnection:
    connection = None
    connection_link = user.get('mongo_link')

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = MongoClient(cls.connection_link)

        return cls.connection
