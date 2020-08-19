from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PhpTravelsSearchResultPageAlzer:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = ''
    PAGE_TITLE = ''

    # Element Locators
    HOTEL_TITLE = (By.XPATH, "//span[@class='text-primary']")

    # Methods

    def load_page(self):
        self.browser.get(self.URL)

    def verify_title(self):
        assert self.browser.title == self.PAGE_TITLE

    def verify_url(self):
        assert self.browser.current_url == self.URL
