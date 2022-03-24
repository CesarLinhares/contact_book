from src.core.status import Status
from src.repository.mongo_actions import RepositoryMongo


class Detail:
    repository_mogo = RepositoryMongo()

    def get_detail(self, _id: str):
        response = self.repository_mogo.find_one(_id)
        if response is None:
            return_json = {"status": Status.error}
        else:
            response.pop("active")
            response.update({"contactId": response.pop('_id')})
            response.update({"status": Status.success})
            return_json = response
        return return_json
