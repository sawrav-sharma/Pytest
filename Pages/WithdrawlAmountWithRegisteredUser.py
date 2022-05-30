import time

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class WithdrawlAmountWithRegisteredUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyAmountWithdrawlWithRedUsers(self):
        self.do_click(Locators.WITHDRAWL_BTN)
        self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        self.do_click(Locators.WITHDRAW_BTN)
