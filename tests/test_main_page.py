import time
import pytest
from pages.main_page import MainPage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    screenshot = browser.save_screenshot('login.png')
    current_url = browser.current_url
    assert screenshot
    assert current_url == 'http://34.141.58.52:8080/#/login'


@pytest.mark.regression
def test_find_type_of_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.find_type_of_pet()
    page.find_cat()


@pytest.mark.regression
def test_find_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.find_pet_name()
    browser.save_screenshot('petname.png')


@pytest.mark.regression
def test_go_to_details(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_details()
    page.add_comment()
    page.click_to_button()
    time.sleep(2)
    browser.save_screenshot('comment.png')


@pytest.mark.smoke()
def test_go_to_profile(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_profile()
