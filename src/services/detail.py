from src.repository.mongo_actions import RepositoryMongo


class Detail:

    def get_detail(self, _id: str):
        return RepositoryMongo().find_one(_id)
