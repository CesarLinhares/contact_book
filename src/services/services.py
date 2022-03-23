from src.repository.mongo_actions import RepositoryMongo


class RegisterContact:
    mongo = RepositoryMongo()

    def register_contact(self, contact: dict):
        return self.mongo.register(contact)


class ContactDetail:
    pass
