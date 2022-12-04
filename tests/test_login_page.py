import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    login = page.go_to_login()
    assert login != 0
    page.go_to_password()
    page.click_to_button()

