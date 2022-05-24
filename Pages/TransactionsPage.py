import time
from datetime import datetime as dt

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Transactions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyCreditTransactions(self):
        nowDateTime = dt.now()
        currentDate = nowDateTime.strftime("%B %d, %Y %I:%M")
        print('\nCurrent date :', currentDate)
        # res = []
        # res[:] = currentDate
        # print(res.pop(13))

        # print(res.pop(5))
        # currentDate = nowDateTime.strftime("%B %d, %Y %-I:%M")
        # # res = [ele.lstrip('0') for ele in currentDate]
        # # print(res)
        # print("Current Date :"+currentDate.lstrip('0'))
        # print(currentDate)
        # print(int(currentDate))
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(3)
        getText = self.get_element_text(Locators.AMOUNT_DEPOSITED)
        time.sleep(3)
        print(getText)
        assert getText == TestData.DEPOSITING_AMOUNT
        getTransactionType = self.get_element_text(Locators.TRANSACTIONS_TYPE_CREDIT)
        print(getTransactionType)
        getCurrentDateTime = self.get_element_text(Locators.TRANSACTIONS_DATE_TIME)
        print("Transaction time :" + getCurrentDateTime.rpartition(':')[0])
        # print(split(getCurrentDateTime))
        assert getCurrentDateTime.text == currentDate
        assert getTransactionType == "Credit"

    def verifyDebitTransactions(self):
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(3)
        getDebText = self.get_element_text(Locators.TRANSACTIONS_TYPE_DEBIT)
        time.sleep(3)
        assert getDebText == "Debit"
