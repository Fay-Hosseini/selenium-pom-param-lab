import pytest

from pages.login_page import LoginPage

#Test data:(username, password, expected_error_substring)
test_data = [
    ("wrong_user","wrong_pass","Your username is invalid!"),
    ("tomsmith","wrong_pass","Your password is invalid!"),
]

@pytest.mark.parametrize("username,password,expected_error",test_data)
def test_login_with_invalid_credentials(driver,username,password,expected_error):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login(username,password)

    error_text = login_page.get_error_message()
    assert expected_error in error_text

"""
Install Allure-related Python packages : pip install allure-pytest

Allure generates nice HTML reports, but it needs its CLI tool installed.:choco install allure

Manual download (if you don’t have choco/brew):
Download from: https://github.com/allure-framework/allure2/releases
Extract the zip
Add the bin folder to your system PATH

Run pytest with Allure results output: pytest --alluredir=allure-results
Generate the HTML report: allure serve allure-results  (This launches a local web server and opens the report in your browser.)


"""