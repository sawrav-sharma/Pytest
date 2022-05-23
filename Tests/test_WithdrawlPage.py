from Pages.CustomerLogin import CustomerLogin
from Pages.DepositPage import DepositPage
from Pages.WithdrawlPage import Withdrawl
from Tests.test_Base import BaseTest


class Test_Withdrawl(BaseTest):

    def test_verifyingWithdrawl(self):
        combineLogin = CustomerLogin(self.driver)
        combineLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
        withdrawnAmnt = Withdrawl(self.driver)
        withdrawnAmnt.verifyWithdrawl()
