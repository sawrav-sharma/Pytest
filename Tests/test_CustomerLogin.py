import sys, os
import time

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.CustomerLogin import CustomerLogin
from Tests.test_Base import BaseTest


class Test_CustomerLogin(BaseTest):

    def test_VerifyCombineLogin(self):
        self.combineLogin = CustomerLogin(self.driver)
        self.combineLogin.customerLoginOption()

    def test_verifyLoginCustomer(self):
        self.custLogin = CustomerLogin(self.driver)
        self.custLogin.verifyingLoginCustomer()
