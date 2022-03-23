from typing import List

from pydantic import BaseModel


class Phone(BaseModel):
    type: str
    number: str


class ContactModel(BaseModel):
    email: str
    address: str
    firstName: str
    lastName: str
    phoneList: List[Phone]
