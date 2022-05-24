from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from selenium.webdriver.support.select import Select

from Pages.DepositPage import DepositPage


class CustomerLogin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def customerLoginOption(self):
        self.do_click(Locators.CUSTOMER_LOGIN)
        Customers = Select(self.driver.find_element_by_xpath(
            "//select[@id='userSelect']"
        ))
        Customers.select_by_visible_text('Harry Potter')
        self.do_click(Locators.CUSTOMER_LOGIN_BTN)

    def verifyingLoginCustomer(self):
        self.do_click(Locators.CUSTOMER_LOGIN)
        Customers = Select(self.driver.find_element_by_xpath(
            "//select[@id='userSelect']"
        ))
        Customers.select_by_visible_text('Harry Potter')
        self.do_click(Locators.CUSTOMER_LOGIN_BTN)
        elementRec = self.get_element_text(Locators.LOGIN_CUST)
        assert elementRec == "Harry Potter"
        return DepositPage(self.driver)
