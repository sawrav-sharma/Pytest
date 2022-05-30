import time

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class DeletionOfCustomer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeleteCustomer(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        self.do_click(Locators.CUSTOMERS)
        # time.sleep(3)
        self.do_send_keys(Locators.SEARCH_CUSTOMERS, TestData.FIRST_NAME)
        # time.sleep(10)
        self.do_click(Locators.DELETE_CUSTOMERS)
