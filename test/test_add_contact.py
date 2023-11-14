from model.contact import Contact


def test_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = (Contact("Ivan", "Ivanovich", "Ivanov", "ivanushka", "test", "test", "678-66-755",
                       "87899877777",
                       "5656 78788 7", "test@gmail.com", "tes4@gmail.com", "13", "13", "November", "1994")
               )
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
