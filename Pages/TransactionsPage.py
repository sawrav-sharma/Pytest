import time

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Transactions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyCreditTransactions(self):
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(10)
        getText = self.get_element_text(Locators.AMOUNT_DEPOSITED)
        time.sleep(10)
        print(getText)
        assert getText == TestData.DEPOSITING_AMOUNT
        # time.sleep(10)
        getTransactionType = self.get_element_text(Locators.TRANSACTIONS_TYPE_CREDIT)
        print(getTransactionType)
        assert getTransactionType == "Credit"

    def verifyDebitTransactions(self):
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(10)
        getDebText = self.get_element_text(Locators.TRANSACTIONS_TYPE_DEBIT)
        time.sleep(10)
        assert getDebText == "Debit"
