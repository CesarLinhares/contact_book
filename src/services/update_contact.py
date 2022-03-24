from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo


class UpdateContact:
    mongo_repository = RepositoryMongo()

    update_status = {
        True: Status.success,
        False: Status.error
    }

    def update_contact(self, _id: str, updates: dict) -> dict:
        update = self.mongo_repository.update(_id, updates)
        return {"status": self.update_status.get(update)}
