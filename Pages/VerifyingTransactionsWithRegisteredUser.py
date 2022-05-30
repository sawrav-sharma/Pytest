import datetime
import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class VerifyingTransactionWithRegisteredUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyTransactionsWithRegUser(self):
        self.do_click(Locators.TRANSACTIONS_BTN)
        nowDateTime = datetime.datetime.now()
        currentDate = nowDateTime.strftime("%B %d, %Y %#I:%M")
        print('\nCurrent date :', currentDate)
        time.sleep(3)
        getText = self.get_element_text(Locators.AMOUNT_DEPOSITED)
        print('\nAmount deposited message :', getText)
        time.sleep(3)
        assert getText == TestData.DEPOSITING_AMOUNT
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        time.sleep(3)
        getTransactionType = self.get_element_text(Locators.TRANSACTIONS_TYPE_CREDIT)
        assert getTransactionType == "Credit"
        # allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        time.sleep(3)
        print('\nTransaction type :', getTransactionType)
        getCurrentDateTime = self.get_element_text(Locators.TRANSACTIONS_DATE_TIME)
        time.sleep(3)
        getTime = getCurrentDateTime.rpartition(':')[0]
        assert getTime == currentDate
        # allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        self.driver.find_element_by_xpath("//button[text()='Home']").click()
        time.sleep(5)

