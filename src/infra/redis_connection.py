from redis import Redis
from src.infra.connection_links import user


class RedisConnection:
    connection = None
    connection_link = user.get('redis_link')

    @classmethod
    def get_connection(cls):
        if not cls.connection:
            cls.connection = Redis.from_url(cls.connection_link)

        return cls.connection


