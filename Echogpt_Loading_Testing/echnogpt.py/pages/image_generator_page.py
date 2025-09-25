from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # ✅ FIXED absolute import

class ImageGeneratorPage(BasePage):
    OCEAN_BREEZE = (By.XPATH, "//div[contains(text(),'Ocean Breeze')]")
    TEAM_LAL = (By.XPATH, "//div[contains(text(),'Team LAL')]")

    def click_ocean_breeze(self):
        self.click(self.OCEAN_BREEZE)

    def click_team_lal(self):
        self.click(self.TEAM_LAL)
