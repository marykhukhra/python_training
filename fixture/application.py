from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path=r'geckodriver.exe')
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path=r'chromedriver.exe')
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path=r'IEDriverServer.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(
                wd.find_elements_by_name("//input[@value='Send e-Mail']")) > 0):
                wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
