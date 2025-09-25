from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    TITLE_TEXT = (By.TAG_NAME, "h1")

    def get_title(self):
        return self.get_text(self.TITLE_TEXT)
