from model.contact import Contact


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id=str(contact.id), firstname=contact.firstname.strip(),lastname=contact.lastname.strip())

    db_list = map(clean, db.get_contact_list())
    sorted_ui_list = sorted(ui_list, key=Contact.id_or_max)
    sorted_db_list = sorted(db_list, key=Contact.id_or_max)
    assert sorted_ui_list == sorted_db_list
