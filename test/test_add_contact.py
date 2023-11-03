from model.contact import Contact


def test_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact("Ivan", "Ivanovich", "Ivanov", "ivanushka", "test", "test", "678-667-55",
                       "87899877777",
                       "5656787887", "test@gmail.com", "13", "November", "1994")
               )
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
