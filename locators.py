from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    TYPE_OF_PET = (By.XPATH, "// *[ @ id = 'pv_id_2'] / div[1] / span[1]")
    PET_CAT = (By.XPATH, '//*[@id="pv_id_2_1"]')
    PET_NAME = (By.ID, "petName")
    DETAILS_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div/div/div[3]/div[1]/button')
    PROFILE_BUTTON = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')
    COMMENT = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[1]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BUTTON = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    CREATE_NEW_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    DELETE_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[3]/div/div[2]/button[2]/span[2]')
    DELETE_PET = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(3) > div:nth-of-type(2) > button:nth-of-type(2)')
    EDIT_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')
    PET_NAME = (By.ID, 'name')
    PET_AGE = (By.CSS_SELECTOR, '#age > input')
    PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    PET_TYPE_CAT = (By.XPATH, '//*[@aria-label="cat"]')
    PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    ADD_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')