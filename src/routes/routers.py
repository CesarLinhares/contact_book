
from fastapi import APIRouter

from src.core.contact_model import ContactModel
from src.services.services import RegisterContact

route = APIRouter(prefix="/v1")


@route.post("/register")
def register(contact: ContactModel):
    service_register = RegisterContact()
    service_register.register_contact(contact.dict())
    return {"Mensagem": "Rota de registro"}


@route.get("/contacts")
def contact_list():
    return {"Mensagem": "Rota para listar todos os contatos"}


@route.get("/contact/{_id}")
def contact_detail(_id):
    return {"Mensagem": f"Rota para listar um contato pelo {_id}"}


@route.get("/contact/{letter}")
def lista_contact_by_letter(letter):
    return {"Mensagem": f"Rota para listar todos os contatos pela {letter}"}


@route.get("/count")
def count_contacts_and_count_number_type_phone():
    return {"Mensagem": f"Rota para exibir o número de contatos e números de telefones por tipo de telefone"}


@route.put("/edit/{_id}")
def edit_contact(_id):
    return {"Mensagem": f"Rota para editar um contato pelo {_id}"}


@route.delete("/remove/{_id}")
def remove_contact(_id):
    return {"Mensagem": f"Rota para excluir um contato pelo {_id}"}

