from redis import Redis

from src.core.interfaces.infrastructure.interface import IConnection
from src.infra.connection_links import user


class RedisConnection(IConnection):
    connection = None
    connection_link = user.get('redis_link')

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = Redis.from_url(cls.connection_link)

        return cls.connection


