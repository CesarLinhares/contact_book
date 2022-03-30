from src.core.interfaces.controller.interface import IController
from src.services.list_service import ListService
from src.services.contact_service import ContactServices


class ContactController(IController):
    lists_services = ListService()
    contact_services = ContactServices()

    @staticmethod
    def register(contact: dict) -> dict:
        return ContactController.contact_services.register(contact)

    @staticmethod
    def update(_id: str, updates: dict) -> dict:
        return ContactController.contact_services.update(_id, updates)

    @staticmethod
    def delete(_id: str) -> dict:
        return ContactController.contact_services.delete(_id)

    @staticmethod
    def get_detail(_id: str) -> dict:
        return ContactController.contact_services.get_detail(_id)

    @staticmethod
    def list_contacts() -> dict:
        return ContactController.lists_services.list_contacts()

    @staticmethod
    def list_contacts_by_letter(letter: str) -> dict:
        return ContactController.lists_services.list_contacts_by_letter(letter)

    @staticmethod
    def count_registers() -> dict:
        return ContactController.lists_services.count_registers()

