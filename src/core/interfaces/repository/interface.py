from abc import ABC, abstractmethod


class IDataBase(ABC):
    connection: any

    @abstractmethod
    def register_a_contact(self, item: any):
        pass
