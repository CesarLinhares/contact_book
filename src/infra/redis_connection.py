from redis import Redis
from src.infra.connection_links import user


class RedisConnection:
    connection = None
    connection_link = user.get('mongo_link')

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = Redis(cls.connection_link)

        return cls.connection
