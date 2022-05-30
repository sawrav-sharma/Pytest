import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Withdrawl(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyWithdrawl(self):
        self.do_click(Locators.WITHDRAWL_BTN)
        time.sleep(3)
        self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        self.do_click(Locators.WITHDRAW_BTN)
        # time.sleep(3)
        # try:
        time.sleep(3)
        capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
        time.sleep(3)
        print('\nCaptured Msg :', capturingWithdrawnSuccessfullyMsg)
        assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        # except TimeoutException:
        #     raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        # except NoSuchElementException:
        #     return "None"
        # except Exception:
        #     return "None"
        '''         
        self.do_click(Locators.WITHDRAWL_BTN)
        amt = self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        # time.sleep(5)
        print(amt)
        self.do_click(Locators.WITHDRAW_BTN)
        time.sleep(5)
        capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
        time.sleep(5)
        print('\nCaptured Msg :', capturingWithdrawnSuccessfullyMsg)
        assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)'''
