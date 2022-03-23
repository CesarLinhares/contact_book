from src.repository.mongo_actions import RepositoryMongo
from src.repository.redis_actions import RepositoryRedis


class RegisterContact:
    mongo_repository = RepositoryMongo()
    redis_repository = RepositoryRedis()

    def register_contact(self, contact: dict):
        return self.mongo_repository.find_one()


class ContactDetail:
    pass

