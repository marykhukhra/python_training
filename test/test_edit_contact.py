def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(new_email="test@g.com")
    app.session.logout()
