import random
import string
from datetime import datetime


class TestData:
    BASE_URL = "https://globalsqa.com/angularJs-protractor/BankingProject/#/login"
    DEPOSITING_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 10))
    SUCCESSFULLY_DEPOSIT_AMT_MSG = "Deposit Successful"
    WITHDRAWL_AMOUNT = ''.join(random.choice(string.digits) for _ in range(1, 5))
    SUCCESSFULL_WITHDRAWN_AMT_MSG = "Transaction successful"
    FIRST_NAME = ''.join(random.choice(string.ascii_letters) for _ in range(1, 10))
    LAST_NAME = ''.join(random.choice(string.ascii_letters) for _ in range(1, 6))
    POST_CODE = ''.join(random.choice(string.digits) for _ in range(1, 5))
    FULL_NAME = FIRST_NAME + " " + LAST_NAME
