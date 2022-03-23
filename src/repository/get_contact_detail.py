from src.repository.mongo_actions import RepositoryMongo


class ContactDetail:
    mongo_repository = RepositoryMongo()

    def get_contact_detail(self, _id: str):
        return self.mongo_repository.find_one(_id)
