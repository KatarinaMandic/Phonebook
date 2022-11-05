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

sg.theme('DarkBlue')

layout1 = [
    [sg.Listbox('', size = (50,20))]
]

layout2 = [
    [sg.Text('Create new User', justification='c', font=('Arial', 24))],
    [sg.Text('')],
    [sg.Text('First name: ', size = (10,1)), sg.Input('', key = '_FNAME_')],
    [sg.Text('Last name: ', size = (10,1)), sg.Input('', key = '_LNAME_')],
    [sg.Text('Telephone: ', size = (10,1)), sg.Input('', key = '_TELEPHONE_')],
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

window.close()