import time

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from Pages.WithdrawlPage import Withdrawl


class DepositPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeposit(self):
        self.do_click(Locators.DEPOSIT_BTN)
        self.do_send_keys(Locators.ADD_AMOUNT, TestData.DEPOSITING_AMOUNT)
        time.sleep(3)
        print(TestData.DEPOSITING_AMOUNT)
        self.do_click(Locators.AFTER_ADDING_AMOUNT_BTN)
        time.sleep(3)
        capturingMsg = self.get_element_text(Locators.DEPOSIT_SUCCESSFULL_MSG)
        print(capturingMsg)
        assert capturingMsg == TestData.SUCCESSFULLY_DEPOSIT_AMT_MSG
        # nowDateTime = datetime.datetime.now()
        # currentDate = nowDateTime.strftime("%B %d, %Y %H:%M:%S %p")
        # print(currentDate)
        return Withdrawl(self.driver)
