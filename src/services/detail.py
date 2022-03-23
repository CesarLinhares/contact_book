from src.repository.get_contact_detail import ContactDetail


class Detail:

    def get_detail(self, _id: str):
        return ContactDetail().get_contact_detail(_id)
