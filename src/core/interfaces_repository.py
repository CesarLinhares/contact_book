from abc import ABC, abstractmethod


class IRepository(ABC):
    connection: any

    @abstractmethod
    def delete(self, _id: str):
        pass

    @abstractmethod
    def register(self, item: any):
        pass


class IMongo(IRepository, ABC):
    @abstractmethod
    def update(self, _id: str, item: dict):
        pass

    @abstractmethod
    def find_one(self, _id: str):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_letter(self, letter: str):
        pass


class IRedis(IRepository, ABC):
    @abstractmethod
    def verify_if_exists(self, key: str):
        pass
