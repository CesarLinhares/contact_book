import psycopg2

from src.core.interfaces.infrastructure.interface import IConnection


class PostgresConnection(IConnection):
    connection = None

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = psycopg2.connect(
                host='localhost',
                database='contacts',
                user='user',
                password='admin'
            )

        return cls.connection
