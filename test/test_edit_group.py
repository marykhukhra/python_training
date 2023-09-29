def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(new_header="gr5")
    app.session.logout()
