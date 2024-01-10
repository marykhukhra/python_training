import re

from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.wd
        self.open_page_add_contact()
        self.contact_parametr(contact)
        # submit contact creation
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home()
        self.contact_cache = None

    def contact_parametr(self, contact):
        driver = self.app.wd
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").send_keys(contact.home_phone)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").send_keys(contact.self_mobile)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("work").send_keys(contact.work_mobile)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").send_keys(contact.phone2)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(str(contact.bday))
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").send_keys(contact.byear)

    def contact_parameter_delete(self):
        driver = self.app.wd
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def select_contact_by_index(self, index):
        # select contact
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_contact_by_id(self, id):
        # select contact
        wd = self.app.wd
        url = "edit.php?id=%s" % id
        wd.find_element_by_xpath('//a[@href="' + url + '"]').click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        contact_name_field = wd.find_element_by_name("firstname")
        contact_name_field.clear()
        contact_name_field.send_keys(contact.firstname)
        contact_name_field = wd.find_element_by_name("lastname")
        contact_name_field.clear()
        contact_name_field.send_keys(contact.lastname)
        wd.find_element_by_name("update").click()
        self.return_to_home()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.select_contact_by_id(id)
        contact_name_field = wd.find_element_by_name("firstname")
        contact_name_field.clear()
        contact_name_field.send_keys(contact.firstname)
        contact_name_field = wd.find_element_by_name("lastname")
        contact_name_field.clear()
        contact_name_field.send_keys(contact.lastname)
        wd.find_element_by_name("update").click()
        self.return_to_home()
        self.contact_cache = None

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def select_for_delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_for_delete_contact_by_id(self, id):
        # select contact
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.wd.find_element_by_link_text("home").click()
        self.select_for_delete_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.wd.find_element_by_link_text("home").click()
        self.select_for_delete_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home()
        self.contact_cache = None

    def return_to_home(self):
        self.app.wd.find_element_by_link_text("home").click()

    def open_page_add_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("add new")) > 0):
            self.app.wd.find_element_by_link_text("add new").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                element_entities = element.find_elements_by_tag_name("td")
                surname = element_entities[1].text
                name = element_entities[2].text
                address = element_entities[3].text
                all_emails = element_entities[4].text
                all_phones = element_entities[5].text
                contact = Contact(firstname=name, lastname=surname, id=id, address=address,
                            all_phones_from_homepage=all_phones,
                            all_emails_from_homepage=all_emails)
                self.contact_cache.append(contact)
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        self_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work_mobile = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, email=email, email2=email2,
                       email3=email3,
                       home_phone=home_phone, self_mobile=self_mobile, work_mobile=work_mobile, phone2=phone2)

    def contact_form_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        self_mobile = re.search("M: (.*)", text).group(1)
        work_mobile = re.search("W: (.*)", text).group(1)
        phone2 = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=home_phone, self_mobile=self_mobile, work_mobile=work_mobile, phone2=phone2)
