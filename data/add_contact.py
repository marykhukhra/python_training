import random
import string

from model.contact import Contact

constant = [
    Contact("Firstname", "middlename", "Lastname", "nikname", "test", "test", "67866755",
            "87899877777",
            "5656787887", "454455", "test@gmail.com", "test@gmail.com", "test@gmail.com", "13",
            "November",
            "1994"),
    Contact("Firstname2", "middlename2", "Lastname2", "nikname2", "test2", "test2", "627866755",
            "287899877777",
            "25656787887", "2454455", "test2@gmail.com", "test2@gmail.com", "test2@gmail.com", "12",
            "October",
            "1992"),
]


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
