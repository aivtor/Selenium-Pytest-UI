import time
import pytest
from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke
def test_log_out(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.log_out()
    screenshot = browser.save_screenshot('logout.png')
    current_url = browser.current_url
    assert screenshot
    assert current_url == 'http://34.141.58.52:8080/#/register'


@pytest.mark.smoke
def test_create_new_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.create_new_pet()
    page.add_pet_name()
    page.add_pet_age()
    page.choose_pet_type()
    page.choose_pet_type_cat()
    page.choose_pet_gender()
    page.choose_pet_gender_male()
    page.submit_add_pet_button()
    page.open()


@pytest.mark.smoke
def test_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(2)
    page.delete_pet_button()
    page.delete_pet()


@pytest.mark.regression
def test_edit_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.edit_pet()
