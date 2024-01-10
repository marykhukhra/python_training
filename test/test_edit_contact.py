import random

from model.contact import Contact


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("","Ivan", "Ivanovich", "Ivanov", "ivanushka", "test", "test", "67866755",
                                   "87899877777",
                                   "5656787887", "454455", "test@gmail.com", "test@gmail.com", "test@gmail.com", "13",
                                   "November",
                                   "1994")
                           )
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id,contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)