from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact("Sergey", "Andreevich", "Ivanov", "ivanushka", "test", "test", "678-667-55",
                                     "7755477",
                                     "5656787887", "test2@gmail.com", "13", "November", "1994")
                             )
    app.session.logout()
