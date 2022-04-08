from abc import ABC, abstractmethod

from src.core.interfaces.repository.interface import IRepository


class IPostgres(IRepository, ABC):
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
