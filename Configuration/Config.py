import random
import string


class TestData:
    BASE_URL = "https://globalsqa.com/angularJs-protractor/BankingProject/#/login"
    REGISTERED_USER = "Albus Dumbledore"
    DEPOSITING_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 10))
    SUCCESSFULLY_DEPOSIT_AMT_MSG = "Deposit Successful"
    WITHDRAWL_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 5))
    SUCCESSFULL_WITHDRAWN_AMT_MSG = "Transaction successful"
    FAILED_WITHDRAWN_MSG = "Transaction Failed. You can not withdraw amount more than the balance."
    FIRST_NAME = ''.join(random.choice(string.ascii_letters) for _ in range(1, 10))
    LAST_NAME = ''.join(random.choice(string.ascii_letters) for _ in range(1, 6))
    POST_CODE = ''.join(random.choice(string.digits) for _ in range(1, 5))
    FULL_NAME = FIRST_NAME + " " + LAST_NAME
