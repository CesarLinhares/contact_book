from src.repository.mongo_actions import RepositoryMongo


class UpdateContact:
    mongo_repository = RepositoryMongo()

    def update_contact(self, _id: str, updates: dict):
        self.mongo_repository.update('_id', updates)
