import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Withdrawl(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyWithdrawl(self):
        try:
            self.do_click(Locators.WITHDRAWL_BTN)
            # time.sleep(5)
            self.do_click(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX)
            self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
            # time.sleep(5)
            print(TestData.WITHDRAWL_AMOUNT)
            self.do_click(Locators.WITHDRAW_BTN)
            # time.sleep(5)
            capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
            # time.sleep(5)
            print('\nCaptured Msg :', capturingWithdrawnSuccessfullyMsg)
            assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        except:
            pass

        # return Transactions(self.driver)

        # try:
        #     self.do_click(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX)
        #     self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        #     time.sleep(3)
        #     self.do_click(Locators.WITHDRAW_BTN)
        #     capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
        #     print('\nWithdrawl successful message :', capturingWithdrawnSuccessfullyMsg.text)
        #     assert capturingWithdrawnSuccessfullyMsg.text == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        # except:
        #     capturingWithdrawlFailedMsg = self.get_element_text(Locators.WITHDRAWL_UNSUCCESSFUL_MSG)
        #     assert capturingWithdrawlFailedMsg.text == TestData.FAILED_WITHDRAWN_MSG
        #     pass
        #     print('\nWithdrawl Failed Message :', capturingWithdrawlFailedMsg.text)
