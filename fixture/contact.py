from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.wd
        self.open_page_add_contact()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
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
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").send_keys(contact.work_mobile)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("new_group").click()
        Select(driver.find_element_by_name("new_group")).select_by_visible_text("group")
        # submit contact creation
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home()

    def return_to_home(self):
        self.app.wd.find_element_by_link_text("home").click()

    def open_page_add_contact(self):
        self.app.wd.find_element_by_link_text("add new").click()