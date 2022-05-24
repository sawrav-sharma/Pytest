from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class ManagerLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def managerLoginOption(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        addCust = self.get_element_text(Locators.ADD_CUSTOMERS)
        print('\nTitle :', addCust)
        assert addCust == "Add Customer"

    def verifyingTitle(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        title = self.get_title()
        print('\nTitle :', title)
        assert title == "XYZ Bank"
