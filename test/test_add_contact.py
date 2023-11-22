import random
import string

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "" * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def get_random_month():
    random_month = random.choice(
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December'])
    return random_month


testdata = [
    Contact(firstname=random_string("firstname", 10),
            middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10),
            company=random_string("company", 10),
            address=random_string("address", 20),
            home_phone=random_string("home_phone", 16),
            self_mobile=random_string("self_mobile", 20),
            work_mobile=random_string("work_mobile", 20),
            phone2=random_string("phone2", 20),
            email=random_string("email", 20),
            email2=random_string("email2", 20),
            email3=random_string("email3", 20), bday=random.randrange(2, 30),
            bmonth=get_random_month(), byear=random_string("", 5),
            )
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
