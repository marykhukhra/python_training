# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application


def test_contact(app):
    app.contact.create(Contact("Ivan", "Ivanovich", "Ivanov", "ivanushka", "test", "test", "678-667-55",
                               "87899877777",
                               "5656787887", "test@gmail.com", "13", "November", "1994")
                       )
