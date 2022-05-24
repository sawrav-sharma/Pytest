import time
from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Customers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyCustomers(self):
        self.do_click(Locators.CUSTOMERS)
        time.sleep(5)
        # cust = self.get_element_text(Locators.VERIFYING_CUSTOMER_USING_POSTCODE)
        # print(cust)
        cust = self.driver.find_element_by_xpath("//td[contains(text(),'%s')]" % int(TestData.POST_CODE))
        print('\nCustomer Post Code :', cust.text)
        assert cust.text == TestData.POST_CODE
