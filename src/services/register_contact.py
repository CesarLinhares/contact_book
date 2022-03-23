from hashlib import md5

from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo
from src.repository.redis_actions import RepositoryRedis


class RegisterContact:
    mongo_repository = RepositoryMongo()
    redis_repository = RepositoryRedis()

    status = {
        True: Status.success,
        False: Status.error
    }

    @staticmethod
    def _contact_modeling(contact: dict) -> dict:
        string_to_make_id = (
            f"{contact.get('firstName') + contact.get('lastName')}:"
            f"{contact.get('email')}:"
        )
        _id = md5(string_to_make_id.encode()).hexdigest()
        contact_modeled = contact
        contact_modeled.update({'_id': str(_id), 'active': True})
        return contact_modeled

    def _update_deleted_contact(self, contact: dict) -> bool:
        clean_redis = self.redis_repository.delete(contact.get('_id'))
        update_mongo = self.mongo_repository.update(contact.get('_id'), {'active': True})
        return clean_redis and update_mongo

    def register_contact(self, contact: dict):
        contact_to_register = self._contact_modeling(contact)

        contact_has_been_deleted = self.redis_repository.verify_if_exists(contact_to_register.get('_id'))
        options_to_contact_deleted = {
            True: lambda x: self._update_deleted_contact(x),
            False: lambda x: self.mongo_repository.register(x)
        }
        register = options_to_contact_deleted.get(contact_has_been_deleted)
        try:
            message = {'status': self.status.get(register(contact_to_register))}
            return message
        except:
            return {'status': self.status.get(False)}


