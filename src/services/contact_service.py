from hashlib import md5

from src.core.enumerator.contact_status import ContactStatus
from src.core.enumerator.status import Status
from src.repository.deleted_user import DeletedUserRepository
# from src.repository.user_data_postgres import UserDataRepository
from src.repository.user_data_mongo import UserDataRepository


class ContactServices:
    user_data_repository = UserDataRepository()
    deleted_user_repository = DeletedUserRepository()

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
        contact_modeled.update({'_id': str(_id), 'active': ContactStatus.ACTIVE.value})
        return contact_modeled

    @staticmethod
    def _detail_model(contact_list: dict) -> dict:
        return_dict = contact_list
        return_dict.pop("active")
        return_dict.update({"contactId": return_dict.pop('_id')})
        return_dict.update({"status": Status.SUCCESS.value})
        return return_dict

    def _update_deleted_contact(self, contact: dict) -> bool:
        clean_cache = self.deleted_user_repository.remove_from_cache(contact.get('_id'))
        update_user = self.user_data_repository.update_a_contact(contact.get('_id'), contact)
        return clean_cache and update_user

    def register(self, contact: dict) -> dict:
        contact_to_register = self._contact_modeling(contact)

        contact_has_been_deleted = self.deleted_user_repository.verify_if_is_cached(contact_to_register.get('_id'))
        options_to_contact_deleted = {
            True: lambda x: self._update_deleted_contact(x),
            False: lambda x: self.user_data_repository.register_a_contact(x)
        }
        register = options_to_contact_deleted.get(contact_has_been_deleted)
        try:
            message = {'status': self.status.get(register(contact_to_register))}
            return message
        except:
            return {'status': self.status.get(False)}

    def update(self, _id: str, updates: dict) -> dict:
        update = self.user_data_repository.update_a_contact(_id, updates)
        return {"status": self.status.get(update)}

    def delete(self, _id: str):
        active_false = self.user_data_repository.update_a_contact(_id, {"active": ContactStatus.INACTIVE.value})
        insert_in_cache = self.deleted_user_repository.register_a_contact(_id)
        deletion_status = active_false and insert_in_cache

        return {"status": self.status.get(deletion_status)}

    def get_detail(self, _id: str):
        response = self.user_data_repository.find_one_contact(_id)

        error_option = {
            True: lambda: {"status": Status.ERROR.value},
            False: lambda: self._detail_model(response)
        }

        action = error_option.get(response is None)

        return action()
