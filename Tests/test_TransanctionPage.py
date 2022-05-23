from Pages.CustomerLogin import CustomerLogin
from Pages.DepositPage import DepositPage
from Pages.TransactionsPage import Transactions
from Pages.WithdrawlPage import Withdrawl
from Tests.test_Base import BaseTest


class Test_Transactions(BaseTest):
    def test_verifyingCreditTransactions(self):
        combineLogin = CustomerLogin(self.driver)
        combineLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
        transaction = Transactions(self.driver)
        transaction.verifyCreditTransactions()

    def test_verifyingDebitTransactions(self):
        combineLogin = CustomerLogin(self.driver)
        combineLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
        withdrawnAmnt = Withdrawl(self.driver)
        withdrawnAmnt.verifyWithdrawl()
        transaction = Transactions(self.driver)
        transaction.verifyDebitTransactions()

