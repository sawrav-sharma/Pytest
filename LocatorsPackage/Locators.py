from selenium.webdriver.common.by import By


class Locators:
    CUSTOMER_LOGIN = (By.XPATH, "//button[text()='Customer Login']")
    BANK_MANAGER_LOGIN = (By.XPATH, "//button[text()='Bank Manager Login']")
    YOUR_NAME = (By.XPATH, "//select[@id='userSelect']")
    CUSTOMER_LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    LOGIN_CUST = (By.XPATH, "//strong[text()=' Welcome ']//span[text()='Harry Potter']")
    '''Deposit'''
    DEPOSIT_BTN = (By.XPATH, "//button[contains(text(),'Deposit')]")
    ADD_AMOUNT = (By.XPATH, "//input[@placeholder='amount']")
    AFTER_ADDING_AMOUNT_BTN = (By.XPATH, "(//button[contains(text(),'Deposit')])[2]")
    DEPOSIT_SUCCESSFULL_MSG = (By.XPATH, "//span[text()='Deposit Successful']")
    '''Transactions'''
    TRANSACTIONS_BTN = (By.XPATH, "//button[contains(text(),'Trans')]")
    TRANSACTIONS_TYPE_CREDIT = (By.XPATH, "//td[contains(text(),'Credit')]")
    TRANSACTIONS_TYPE_DEBIT = (By.XPATH, "//td[contains(text(),'Debit')]")
    AMOUNT_DEPOSITED = (By.XPATH, "(//tr[@id='anchor0']//td[@class='ng-binding'])[2]")
    AMOUNT_WITHDRAWN = (By.XPATH, "(//tr[@id='anchor0']//td[@class='ng-binding'])[2]")
    '''Withdrawl'''
    WITHDRAWL_BTN = (By.XPATH, "//button[contains(text(),'Withdrawl')]")
    AMOUNT_TO_BE_WITHDRAWN_TEXTBOX = (By.XPATH, "//div[@class='form-group']//input[@placeholder='amount']")
    WITHDRAW_BTN = (By.XPATH, "//button[text()='Withdraw']")
    WITHDRAWL_SUCCESSFULL_MSG = (By.XPATH, "//span[text()='Transaction successful']")
