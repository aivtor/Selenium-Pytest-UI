from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def find_type_of_pet(self):
        type_of_pet_link = self.browser.find_element(*MainPageLocators.TYPE_OF_PET)
        type_of_pet_link.click()

    def find_cat(self):
        pet_cat = self.browser.find_element(*MainPageLocators.PET_CAT)
        pet_cat.click()

    def find_pet_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.PET_NAME)
        pet_name.send_keys('Zuza')
        pet_name.send_keys(Keys.RETURN)

    def go_to_details(self):
        details_link = self.browser.find_element(*MainPageLocators.DETAILS_BUTTON)
        details_link.click()

    def add_comment(self):
        comment_link = self.browser.find_element(*MainPageLocators.COMMENT)
        comment_link.send_keys('Nice pet')
        comment_link.send_keys(Keys.RETURN)

    def click_to_button(self):
        click_button = self.browser.find_element(*MainPageLocators.SAVE_BUTTON)
        click_button.click()

    def go_to_profile(self):
        profile_link = self.browser.find_element(*MainPageLocators.PROFILE_BUTTON)
        profile_link.click()


