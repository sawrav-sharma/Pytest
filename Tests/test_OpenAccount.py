from Pages.AddCustomer import AddCustomer
from Pages.ManagerLogin import ManagerLogin
from Pages.OpenAccount import OpenAccount
from Tests.test_Base import BaseTest


class Test_OpenAccount(BaseTest):

    def test_verifyAccountOpen(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
