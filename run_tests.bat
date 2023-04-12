@echo off

REM Install dependencies
pip install -r requirements.txt

REM Run tests
pytest --junitxml=pytest.xml

echo Running tests...

pytest --alluredir=Allure-Report Tests/

echo Opening Allure report...

allure serve Allure-Report
