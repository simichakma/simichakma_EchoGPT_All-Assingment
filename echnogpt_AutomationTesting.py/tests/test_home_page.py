from pages.home_page import HomePage

def test_navigate(driver):
    home = HomePage(driver)
    home.visit("https://echogpt.live")

    home.click("image")
    assert "image" in driver.current_url.lower()
