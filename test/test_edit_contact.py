from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Andrey1", lastname="Petrov")
                           )
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Andrey1", lastname="Petrov")
    contact.id = old_contacts[1].id
    app.contact.edit_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[1] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


