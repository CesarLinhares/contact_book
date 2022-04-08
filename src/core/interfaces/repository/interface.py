from abc import ABC, abstractmethod


class IRepository(ABC):
    connection: any

    @abstractmethod
    def register(self, item: any):
        pass
