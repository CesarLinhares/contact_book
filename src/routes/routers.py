
from fastapi import APIRouter

from src.core.contact_model import ContactModel
from src.services.list_all_contacts import ListAllContacts
from src.services.list_contacts_by_letter import ListContactsByLetter
from src.services.register_contact import RegisterContact
from src.services.update_contact import UpdateContact

route = APIRouter(prefix="/v1")


@route.post("/register")
def register(contact: ContactModel):
    service_register = RegisterContact()
    return service_register.register_contact(contact.dict())


@route.get("/contacts")
def contact_list():
    list_service = ListAllContacts()
    return list_service.list_contacts()


@route.get("/contact/{_id}")
def contact_detail(_id):
    return Detail().get_detail(str(_id))


@route.get("/contacts/{letter}")
def lista_contact_by_letter(letter: str):
    list_service = ListContactsByLetter()
    return list_service.list_contacts(letter)


@route.get("/count")
def count_contacts_and_count_number_type_phone():
    return {"Mensagem": f"Rota para exibir o número de contatos e números de telefones por tipo de telefone"}


@route.put("/edit/{_id}")
def edit_contact(_id: str, updates: dict):
    service_edit = UpdateContact()
    return service_edit.update_contact(_id, updates)


@route.delete("/remove/{_id}")
def remove_contact(_id):
    return RemoveContact().deleted(str(_id))

