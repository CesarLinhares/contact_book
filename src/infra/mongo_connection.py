from pymongo import MongoClient

from src.core.interfaces_infra import IConnection
from src.infra.connection_links import user


class MongoConnection(IConnection):
    connection = None
    connection_link = user.get('mongo_link')

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = MongoClient(cls.connection_link)

        return cls.connection
