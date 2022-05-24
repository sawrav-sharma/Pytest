import time
from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from Pages.TransactionsPage import Transactions


class Withdrawl(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyWithdrawl(self):
        self.do_click(Locators.WITHDRAWL_BTN)
        time.sleep(5)
        self.do_click(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX)
        self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        time.sleep(5)
        print(TestData.WITHDRAWL_AMOUNT)
        self.do_click(Locators.WITHDRAW_BTN)
        time.sleep(5)
        capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFULL_MSG)
        time.sleep(5)
        print(capturingWithdrawnSuccessfullyMsg)
        assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        return Transactions(self.driver)

        # try:
        #     self.do_click(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX)
        #     self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        #     time.sleep(15)
        #     # print(TestData.WITHDRAWL_AMOUNT)
        #     self.do_click(Locators.WITHDRAW_BTN)
        #     time.sleep(5)
        #     capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFULL_MSG)
        #     time.sleep(5)
        #     print(capturingWithdrawnSuccessfullyMsg)
        #     assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        # except "Not enough bank balance":
        #     pass
        # raise Exception("Not enough money")
        # return Transactions(self.driver)
