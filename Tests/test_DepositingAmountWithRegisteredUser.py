from Pages.DepositingAmountWithRegisteredUser import DepositingAmountWithRegisteredUser
from Pages.LoginWithRegisteredUsers import LoginWithRegisteredUser
from Tests.test_Base import BaseTest


class Test_DepositingAmountWithRegisteredUser(BaseTest):
    def test_verifyDepositAmountWithRegUser(self):
        registerCust = LoginWithRegisteredUser(self.driver)
        registerCust.logIn()
        depoAmount = DepositingAmountWithRegisteredUser(self.driver)
        depoAmount.verifyDepoAmountWithRegisteredUser()
