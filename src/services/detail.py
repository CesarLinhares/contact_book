from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo


class Detail:
    repository_mogo = RepositoryMongo()

    def answer_model(self, contact_list: dict) -> dict:
        return_dict = contact_list
        return_dict.pop("active")
        return_dict.update({"contactId": return_dict.pop('_id')})
        return_dict.update({"status": Status.success})
        return return_dict

    def get_detail(self, _id: str):
        response = self.repository_mogo.find_one(_id)

        error_option = {
            True: lambda: {"status": Status.error},
            False: lambda: self.answer_model(response)
        }

        action = error_option.get(response is None)

        return action()
