from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo


class ListContactsByLetter:
    mongo_repository = RepositoryMongo()

    list_status = {
        True: Status.success,
        False: Status.error
    }

    def list_contacts(self, letter: str) -> dict:
        contact_list = self.mongo_repository.find_by_letter(letter.lower())
        success = bool(len(contact_list))

        for contact in contact_list:
            contact.pop('active')

        dict_of_contact_list = {
            "contactsList": contact_list,
            "status": self.list_status.get(success)
        }
        return dict_of_contact_list
