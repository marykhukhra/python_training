from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact("Andrey", "Andreevich", "Petrov", "ivanushka", "test", "test", "678-667-55",
                                     "7755477",
                                     "5656787887", "test2@gmail.com", "13", "November", "1994")
                             )
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_contact(Contact("Sergey", "Andreevich", "Ivanov", "ivanushka", "test", "test", "678-667-55",
                                     "7755477",
                                     "5656787887", "test2@gmail.com", "13", "November", "1994")
                             )
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)