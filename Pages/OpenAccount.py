import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from selenium.webdriver.support.select import Select


class OpenAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyOpenAccount(self):
        self.do_click(Locators.OPEN_ACCOUNT)
        customers = Select(self.driver.find_element_by_xpath("//select[@name='userSelect']"))
        customers.select_by_visible_text(TestData.FULL_NAME)
        print(TestData.FULL_NAME)
        currency = Select(self.driver.find_element_by_xpath("//select[@id='currency']"))
        currency.select_by_visible_text("Dollar")
        self.do_click(Locators.PROCESS_BTN)
        # time.sleep(3)
        alertHandle = self.driver.switch_to.alert
        alertHandle.accept()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        # allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        # try:
        #     self.driver.find_element_by_xpath("//button[contains(text(),'Ok')]")
        #     alertHandle = self.driver.switch_to.alert
        #     alertHandle.accept()
        # except:
        #     pass
