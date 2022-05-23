from Pages.CustomerLogin import CustomerLogin
from Pages.DepositPage import DepositPage
from Tests.test_Base import BaseTest


class Test_Deposit(BaseTest):
    def test_verifyDeposit(self):
        combineLogin = CustomerLogin(self.driver)
        combineLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
