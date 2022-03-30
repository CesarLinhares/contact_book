from abc import ABC, abstractmethod


class IRepository(ABC):
    connection: any

    @abstractmethod
    def delete(self, _id: str):
        pass

    @abstractmethod
    def register(self, item: any):
        pass
