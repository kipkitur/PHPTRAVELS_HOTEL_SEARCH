from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PhpTravelsSearchResultPageTria:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = ''
    PAGE_TITLE = ''

    # Element Locators
    HOTEL_TITLE = (By.XPATH, "//h2[@id='detail-content-sticky-nav-00'")

    # Methods

    def load_page(self):
        self.browser.get(self.URL)

    def verify_title(self, item):
        assert self.browser.title == self.PAGE_TITLE + item

    def verify_url(self):
        assert self.browser.current_url == self.URL