# Korišćenje PySimpleGUI biblioteke kreirati aplikaciju za telefonski
# imenik. Interfejs ima deo za unos kontakta (ime, prezime, broj telefona,
# mail) i deo za prikaz unetih kontakata u imenik.
# • Svaki novi unos treba da bude kreiran kao objekat klase Kontakt. Klasu
# proizvoljno kreirajte da poseduje potrebne podatke i metode.
# • Svaki kreirani kontakt prikazuje se posle kreiranja u delu za prikaz
# kontakata.
# • Svi kontakti se snimaju u serijalizovanoj datoteci imenik.ser.
# • Pri pokretanju aplikacije učitavaju se prethodno snimljeni kontakti.

import PySimpleGUI as sg
from contacts.Validator import Validator
from contacts.Contact import Contact

sg.theme('DarkBlue')

layout1 = [
    [sg.Listbox(Contact.get_all_contacts().values(), size = (50,20), key = '_CONTACTS_')]
]

layout2 = [
    [sg.Text('Create new User', justification='c', font=('Arial', 24))],
    [sg.Text('')],
    [sg.Text('First name: ', size = (10,1)), sg.Input('', key = '_FNAME_')],
    [sg.Text('Last name: ', size = (10,1)), sg.Input('', key = '_LNAME_')],
    [sg.Text('Telephone: ', size = (10,1)), sg.Input('example: +XXX XX XXX XXX(X)',  key = '_TELEPHONE_', do_not_clear=False)],
    [sg.Text('E-mail: ', size = (10,1)), sg.Input('', key = '_EMAIL_')],
    [sg.Text('')],
    [sg.Text('', size = (39,1)), sg.Button('Save', size=(10, 1))]
]

layout = [
    [sg.Column(layout=layout1), sg.Column(layout=layout2)]

]

window = sg.Window(title = 'Phonebook', layout=layout)

while True:
    event, values = window.read()
    if event == None:
        break
    if event == 'Save':
        try:
            Validator.check_telephone(values['_TELEPHONE_'])
            Validator.check_email(values['_EMAIL_'])
            new_id = Contact.get_id()
            new_contact = Contact(new_id, values['_FNAME_'], values['_LNAME_'], values['_TELEPHONE_'], values['_EMAIL_'])
            Contact.save_contact(new_contact)
            sg.popup('Contact saved')
            contacts = Contact.get_all_contacts()
            contacts = contacts.values()
            window['_CONTACTS_'].Update(contacts)
        except Exception as ex:
            sg.popup_error(str(ex), title = 'Error')

window.close()