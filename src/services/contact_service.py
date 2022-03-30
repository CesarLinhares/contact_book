from hashlib import md5

from src.core.enumerator.status import Status
from src.repository.mongo_actions import RepositoryMongo
from src.repository.redis_actions import RepositoryRedis


class ContactServices:
    mongo_repository = RepositoryMongo()
    redis_repository = RepositoryRedis()

    status = {
        True: Status.SUCCESS.value,
        False: Status.ERROR.value
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

    @staticmethod
    def _detail_model(contact_list: dict) -> dict:
        return_dict = contact_list
        return_dict.pop("active")
        return_dict.update({"contactId": return_dict.pop('_id')})
        return_dict.update({"status": Status.SUCCESS.value})
        return return_dict

    def _update_deleted_contact(self, contact: dict) -> bool:
        clean_redis = self.redis_repository.delete(contact.get('_id'))
        update_mongo = self.mongo_repository.update(contact.get('_id'), contact)
        return clean_redis and update_mongo

    def register(self, contact: dict) -> dict:
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

    def update(self, _id: str, updates: dict) -> dict:
        update = self.mongo_repository.update(_id, updates)
        return {"status": self.status.get(update)}

    def delete(self, _id: str):
        active_false = self.mongo_repository.update(_id, {"active": False})
        insert_redis = self.redis_repository.register(_id)
        deletion_status = active_false and insert_redis

        return {"status": self.status.get(deletion_status)}

    def get_detail(self, _id: str):
        response = self.mongo_repository.find_one(_id)

        error_option = {
            True: lambda: {"status": Status.ERROR.value},
            False: lambda: self._detail_model(response)
        }

        action = error_option.get(response is None)

        return action()
