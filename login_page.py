from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Авторизация пользователя"""
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('alena@mail.ru')
        return login_email

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys('123456')

    def click_to_button(self):
        click_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        click_button.submit()

