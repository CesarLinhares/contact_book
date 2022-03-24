from src.repository.mongo_actions import RepositoryMongo


class Detail:
    repository_mogo = RepositoryMongo()
    def get_detail(self, _id: str):
        response = self.repository_mogo.find_one(_id)
        if response is None:
            return_json = {"status": "1004"}
        else:
            response.pop("active")
            response.update({"status": "1001"})
            return_json = response
        return return_json
