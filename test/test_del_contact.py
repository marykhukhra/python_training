from random import randrange

from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("Andrey", "Andreevich", "Petrov", "ivanushka", "test", "test", "67866755",
                                   "7755477",
                                   "5656787887", "45455", "test2@gmail.com", "test2@gmail.com", "test2@gmail.com", "13",
                                   "November", "1994"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
