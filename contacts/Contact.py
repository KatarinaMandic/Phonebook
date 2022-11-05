import pickle
import os

class Contact:

    CONTACTS_FOLDER = './contacts/phonebook/'

    def __init__(self,id, first_name, last_name, telephone, email, **kwargs) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.email = email

    def __str__(self) -> str:
        return f"[{self.id}] {self.first_name} {self.last_name} ({self.telephone})/({self.email})"

    @staticmethod
    def get_path (id):
        return Contact.CONTACTS_FOLDER+'contact_'+str(id)+'.ser'

    @staticmethod
    def save_contact (contact):
        path = Contact.get_path(contact.id)
        with open (path, 'wb') as f:
            pickle.dump(contact, f)

    @staticmethod
    def get_id ():
        contacts = Contact.get_all_contacts()
        return len(contacts)+1

    @staticmethod
    def get_all_contacts():
        files = os.listdir(Contact.CONTACTS_FOLDER)
        contacts = {}
        for file in files:
            path = Contact.CONTACTS_FOLDER+file
            with open(path, 'rb') as f:
                contact = pickle.load(f)
                contacts[contact.id] = Contact(contact.id, contact.first_name, 
                                               contact.last_name, contact.telephone, 
                                               contact.email)

        return contacts

        