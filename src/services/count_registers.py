from src.repository.mongo_actions import RepositoryMongo


class Count:

    def countContactAndPhoneType(self):
        response = RepositoryMongo().find_all()
        numContact = []
        numTypePhones = []
        for contact in response:
            numContact.append(contact['firstName'])
            for phone in contact['phoneList']:
                numTypePhones.append(phone['type'])

        if response == []:
            return_json = {"status": "1004"}
        else:
            return_json = {
                "countContacts": len(numContact),
                "countType": [
                    {
                        "_id": "residential",
                        "Count": numTypePhones.count("residential")
                    },
                    {
                        "_id": "mobile",
                        "Count": numTypePhones.count("mobile")
                    },
                    {
                        "_id": "commercial",
                        "Count": numTypePhones.count("commercial")
                    }
                ],
                "status": "1001"
            }
        return return_json


teste = Count()
print(teste.countContactAndPhoneType())
