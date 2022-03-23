from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo
from src.repository.redis_actions import RepositoryRedis


class RemoveContact:
    mongo_repository = RepositoryMongo()
    redis_repository = RepositoryRedis()

    def deleted(self, _id: str):
        active_false = RepositoryMongo().update(_id, {"active": False})
        insert_redis = RepositoryRedis().register(_id)
        deu_bom = active_false and insert_redis
        response = {
            True: Status.success.value,
            False: Status.error.value
        }
        return {"status": response[deu_bom]}
