from pages.home_page import HomePage
from pages.image_generator_page import ImageGeneratorPage

def test_click_images(driver):
    home = HomePage(driver)
    home.visit("https://echogpt.live")
    home.click("image")

    images = ImageGeneratorPage(driver)
    images.click_ocean_breeze()
    images.click_team_lal()
    # Add assertion later (like checking modal or new page opens)

