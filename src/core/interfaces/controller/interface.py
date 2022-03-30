from abc import ABC, abstractmethod


class IController(ABC):
    @staticmethod
    @abstractmethod
    def register(contact: dict) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def update(_id: str, updates: dict) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def delete(_id: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def get_detail(_id: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def list_contacts() -> dict:
        pass

    @staticmethod
    @abstractmethod
    def list_contacts_by_letter(letter: str) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def count_registers() -> dict:
        pass
