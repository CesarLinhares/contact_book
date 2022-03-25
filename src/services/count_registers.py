from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo


class Count:
    instance_mongo = RepositoryMongo()
    count_status = {
        True: Status.success,
        False: Status.error
    }

    def count_contact_and_phone_type(self):
        response = self.instance_mongo.find_all()

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
            "status": self.count_status.get(status)
        }

        return return_json

