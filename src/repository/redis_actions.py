from redis.client import Redis

from src.core.interfaces.repository.deleted_contact_cache.interface import IDeleteCache
from src.infra.redis_connection import RedisConnection


class RepositoryRedis(IDeleteCache):
    connection_infra = RedisConnection()
    connection: Redis = connection_infra.get_connection()

    def remove_from_cache(self, key: str) -> bool:
        return bool(self.connection.delete(key))

    def register_a_contact(self, key: str) -> bool:
        return self.connection.set(key, 1)

    def verify_if_is_cached(self, key: str) -> bool:
        return bool(self.connection.exists(key))
