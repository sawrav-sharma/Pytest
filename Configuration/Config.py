import random
import string


class TestData:
    BASE_URL = "https://globalsqa.com/angularJs-protractor/BankingProject/#/login"
    DEPOSITING_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 10))
    SUCCESSFULLY_DEPOSIT_AMT_MSG = "Deposit Successful"
    WITHDRAWL_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 5))
    SUCCESSFULL_WITHDRAWN_AMT_MSG = "Transaction successful"
