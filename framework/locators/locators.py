from selenium.webdriver.common.by import By

# PREVIEW LOCATORS
BUTTON_GO_TO_ADMIN = (By.CSS_SELECTOR, '.btn.btn-primary.my-2')

# LOGIN PAGE LOCATORS
INPUT_LOGIN = (By.CSS_SELECTOR, '[id="id_username"]')
INPUT_PASSWD = (By.CSS_SELECTOR, '[name="password"]')
BUTTON_LOGIN = (By.CSS_SELECTOR, '[type="submit"]')

# ADMIN PAGE LOCATORS
BUTTON_GROUPS = (By.XPATH, '//a[text()="Groups"]')
GROUPS_NAME_TEST = (By.XPATH, '//a[text()="Test"]')
BUTTON_GO = (By.CSS_SELECTOR, '[class="button"]')
GROUPS_TITLE = (By.CSS_SELECTOR, "#content>h2")
USER_ADD = (By.CSS_SELECTOR, '.model-user :nth-child(2)>a')

# USER PAGE LOCATORS
INPUT_USER_NAME = (By.CSS_SELECTOR, '[id="id_username"]')
INPUT_PASSWORD = (By.CSS_SELECTOR, '[id="id_password1"]')
INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[id="id_password2"]')
BUTTON_SAVE = (By.CSS_SELECTOR, '.submit-row>:nth-child(1)')
GROUPS_FORM = (By.CSS_SELECTOR, '[id="id_groups_from"]')
BUTTON_CHOOSE = (By.CSS_SELECTOR, '[id="id_groups_add_link"]')