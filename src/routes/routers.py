
from fastapi import APIRouter

from src.controller.controller import ContactController
from src.core.validation.contact_model import ContactModel


route = APIRouter(prefix="/v1")


@route.post("/register")
def register(contact: ContactModel):
    return ContactController.register(contact.dict())


@route.get("/contacts")
def contact_list():
    return ContactController.list_contacts()


@route.get("/contact/{_id}")
def contact_detail(_id):
    return ContactController.get_detail(str(_id))


@route.get("/contacts/{letter}")
def lista_contact_by_letter(letter: str):
    return ContactController.list_contacts_by_letter(letter)


@route.get("/count")
def count_contacts_and_count_number_type_phone():
    return ContactController.count_registers()


@route.put("/edit/{_id}")
def edit_contact(_id: str, updates: dict):
    return ContactController.update(_id, updates)


@route.delete("/remove/{_id}")
def remove_contact(_id):
    return ContactController.delete(str(_id))

