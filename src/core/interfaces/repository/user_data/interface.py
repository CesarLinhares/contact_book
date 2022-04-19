from abc import ABC, abstractmethod

from src.core.interfaces.repository.interface import IDataBase


class IUserData(IDataBase, ABC):
    @abstractmethod
    def update_a_contact(self, _id: str, item: dict):
        pass

    @abstractmethod
    def find_one_contact(self, _id: str):
        pass

    @abstractmethod
    def find_all_contacts(self):
        pass

    @abstractmethod
    def find_contacts_by_letter(self, letter: str):
        pass
