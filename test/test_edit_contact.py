from random import randrange
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("Andrey", "Petrov", "Andreevich", "ivanushka", "test", "test", "678-667-55",
                                   "7755477",
                                   "5656787887", "test2@gmail.com", "13", "November", "1994")
                           )
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrey123", lastname="Petrov123")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
