from src.core.enumerator.status import Status
from src.repository.postgres_actions import RepositoryPostgres


class ListService:
    mongo_repository = RepositoryPostgres()

    list_status = {
        True: Status.SUCCESS.value,
        False: Status.ERROR.value
    }

    def list_contacts(self) -> dict:
        contact_list = self.mongo_repository.find_all()
        success = bool(contact_list)

        for contact in contact_list:
            contact.pop('active')
            contact.pop('address')
            contact.update({"contactId": contact.pop('_id')})

        dict_of_contact_list = {
            "contactsList": contact_list,
            "status": self.list_status.get(success)
        }
        return dict_of_contact_list

    def list_contacts_by_letter(self, letter: str) -> dict:
        contact_list = self.mongo_repository.find_by_letter(letter.lower())
        success = bool(contact_list)

        for contact in contact_list:
            contact.pop('active')
            contact.pop('address')
            contact.update({"contactId": contact.pop('_id')})

        dict_of_contact_list = {
            "contactsList": contact_list,
            "status": self.list_status.get(success)
        }
        return dict_of_contact_list

    def count_registers(self):
        response = self.mongo_repository.find_all()

        num_contact = []
        num_type_phones = []

        for contact in response:
            num_contact.append(contact['firstName'])
            for phone in contact['phoneList']:
                num_type_phones.append(phone['type'])

        status = bool(response)

        return_json = {
            "countContacts": len(num_contact),
            "countType": [
                {
                    "_id": "residential",
                    "Count": num_type_phones.count("residential")
                },
                {
                    "_id": "mobile",
                    "Count": num_type_phones.count("mobile")
                },
                {
                    "_id": "commercial",
                    "Count": num_type_phones.count("commercial")
                }
            ],
            "status": self.list_status.get(status)
        }

        return return_json
