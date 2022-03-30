from redis.client import Redis

from src.core.interfaces.repository.redis.interface import IRedis
from src.infra.redis_connection import RedisConnection


class RepositoryRedis(IRedis):
    connection_infra = RedisConnection()
    connection: Redis = connection_infra.get_connection()

    def delete(self, key: str) -> bool:
        return bool(self.connection.delete(key))

    def register(self, key: str) -> bool:
        return self.connection.set(key, 1)

    def verify_if_exists(self, key: str) -> bool:
        return bool(self.connection.exists(key))
