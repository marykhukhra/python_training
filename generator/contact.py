import getopt
import os.path
import random
import string
import sys

import jsonpickle

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            bmonth=get_random_month(), byear=random.randrange(1950, 2023),
            )
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
