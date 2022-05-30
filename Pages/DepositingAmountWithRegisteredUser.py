import time

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class DepositingAmountWithRegisteredUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDepoAmountWithRegisteredUser(self):
        self.do_click(Locators.DEPOSIT_BTN)
        self.do_send_keys(Locators.ADD_AMOUNT, TestData.DEPOSITING_AMOUNT)
        time.sleep(5)
        self.do_click(Locators.AFTER_ADDING_AMOUNT_BTN)
