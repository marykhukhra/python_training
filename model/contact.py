from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 home_phone=None, self_mobile=None,
                 work_mobile=None, phone2=None,
                 email=None, email2=None, email3=None, bday=None, bmonth=None, byear=None,
                 all_emails_from_homepage=None, all_phones_from_homepage=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.self_mobile = self_mobile
        self.work_mobile = work_mobile
        self.phone2 =phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.all_phones_from_homepage = all_phones_from_homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
                self.firstname == other.firstname) and (self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
