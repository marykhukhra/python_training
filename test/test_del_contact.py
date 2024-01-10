import random

from model.contact import Contact


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("","Andrey", "Andreevich", "Petrov", "ivanushka", "test", "test", "67866755",
                                   "7755477",
                                   "5656787887", "45455", "test2@gmail.com", "test2@gmail.com", "test2@gmail.com", "13",
                                   "November", "1994"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        sorted_new_contact = sorted(new_contacts, key=Contact.id_or_max)
        sorted_ui_contact = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
        assert sorted_new_contact == sorted_ui_contact