@echo off

echo Running tests...

pytest --alluredir=Allure-Report Tests/

echo Opening Allure report...

allure serve Allure-Report
