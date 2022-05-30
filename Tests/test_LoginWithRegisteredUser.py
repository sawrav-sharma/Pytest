import pytest

from Pages.LoginWithRegisteredUsers import LoginWithRegisteredUser
from Tests.test_Base import BaseTest


class Test_LoginWithRegisteredUser(BaseTest):

    def test_verifyLoginWithRegisteredUsers(self):
        registerCust = LoginWithRegisteredUser(self.driver)
        registerCust.logIn()
