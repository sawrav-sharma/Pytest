import time

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
        time.sleep(5)
        self.do_click(Locators.PROCESS_BTN)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(),'Ok')]")
            alertHandle = self.driver.switch_to.alert
            alertHandle.accept()
            # alertHandle.wait_for_and_accept_alert()
            alertHandle.self.wait_for_and_switch_to_alert()
        except:
            pass
