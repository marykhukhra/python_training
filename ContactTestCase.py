# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact_test_case(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact("Ivan", "Ivanovich", "Ivanov", "ivanushka", "test", "test", "678-667-55",
                               "87899877777",
                               "5656787887", "test@gmail.com", "13", "November", "1994")
                       )
    app.logout()
