from src.repository.mongo_actions import RepositoryMongo
from src.repository.redis_actions import RepositoryRedis
from src.repository.get_contact_detail import ContactDetail


class RemoveContact:
    mongo_repository = RepositoryMongo()
    redis_repository = RepositoryRedis()

    def deleted(self, _id: str):
        # Pegar os dados no mongo
        user = ContactDetail().get_contact_detail(_id)
        # Atualizar o campo active para false
        user
        # gravar no redis a chave sendo o id e o valor sendo o json
        return user
