from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PhpTravelsSearchResultPageAlzer:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
<<<<<<< HEAD
    URL_SEARCH_FIRST = 'https://www.phptravels.net/hotels/detail/istanbul/alzer-hotel-istanbuls/29-10-2020/31-10-2020/2/0'
    URL_SEARCH_SECOND = 'https://www.phptravels.net/hotels/detail/istanbul/alzer-hotel-istanbuls/29-12-2019/12-31-2019/0/0'
    URL_SEARCH_THIRD = 'https://www.phptravels.net/hotels/detail/istanbul/alzer-hotel-istanbuls/30-12-2020/29-12-2020/2/2'
    PAGE_TITLE_SEARCH_DEFAULT = 'Search Results'
=======
    URL = ''
    PAGE_TITLE = ''
>>>>>>> 601062a313790068a2e4e9f74a256325e65ec794

    # Element Locators
    HOTEL_TITLE = (By.XPATH, "//span[@class='text-primary']")

    # Methods

<<<<<<< HEAD
    def load_page_result(self):
        self.browser.get(self.URL_SEARCH_FIRST)
        self.browser.get(self.URL_SEARCH_SECOND)
        self.browser.get(self.URL_SEARCH_THIRD)

    def verify_title_result(self):
        assert self.browser.title == self.PAGE_TITLE_SEARCH_DEFAULT

    def verify_url_result_first(self):
        assert self.browser.current_url == self.URL_SEARCH_FIRST
    def verify_url_result_second(self):
        assert self.browser.current_url == self.URL_SEARCH_SECOND
    def verify_url_result_third(self):
        assert self.browser.current_url == self.URL_SEARCH_THIRD
=======
    def load_page(self):
        self.browser.get(self.URL)

    def verify_title(self):
        assert self.browser.title == self.PAGE_TITLE

    def verify_url(self):
        assert self.browser.current_url == self.URL
>>>>>>> 601062a313790068a2e4e9f74a256325e65ec794
