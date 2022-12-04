from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def log_out(self):
        log_out_button = self.browser.find_element(*ProfilePageLocators.LOGOUT_BUTTON)
        log_out_button.click()

    def create_new_pet(self):
        create_new_pet_button = self.browser.find_element(*ProfilePageLocators.CREATE_NEW_PET_BUTTON)
        create_new_pet_button.click()

    def add_pet_name(self):
        add_pet_name = self.browser.find_element(*ProfilePageLocators.PET_NAME)
        add_pet_name.send_keys('My new pet')

    def add_pet_age(self):
        add_pet_age = self.browser.find_element(*ProfilePageLocators.PET_AGE)
        add_pet_age.send_keys('1')

    def choose_pet_type(self):
        choose_pet_type = self.browser.find_element(*ProfilePageLocators.PET_TYPE)
        choose_pet_type.click()

    def choose_pet_type_cat(self):
        choose_pet_type_dog = self.browser.find_element(*ProfilePageLocators.PET_TYPE_CAT)
        choose_pet_type_dog.click()

    def choose_pet_gender(self):
        choose_pet_gender = self.browser.find_element(*ProfilePageLocators.PET_GENDER)
        choose_pet_gender.click()

    def choose_pet_gender_male(self):
        choose_pet_gender_male = self.browser.find_element(*ProfilePageLocators.PET_GENDER_MALE)
        choose_pet_gender_male.click()

    def submit_add_pet_button(self):
        submit_add_pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
        submit_add_pet_button.click()

    def delete_pet_button(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON)
        delete_pet_button.click()

    def delete_pet(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET)
        delete_pet_button.click()

    def edit_pet(self):
        edit_pet_button = self.browser.find_element(*ProfilePageLocators.EDIT_PET_BUTTON)
        edit_pet_button.click()
