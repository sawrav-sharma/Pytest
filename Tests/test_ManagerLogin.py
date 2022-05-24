from Pages.ManagerLogin import ManagerLogin
from Tests.test_Base import BaseTest


class Test_ManagerLogin(BaseTest):

    def test_verifyingManagerLogin(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()

    def test_verifyTitle(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.verifyingTitle()
