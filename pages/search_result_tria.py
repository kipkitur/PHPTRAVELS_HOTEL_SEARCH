from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PhpTravelsSearchResultPageTria:

    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL_SEARCH_FIRST_TRIA = 'https://www.phptravels.net/hotels/detail/istanbul/tria-hotel-istanbul-special/29-10-2020/31-10-2020/2/0'
    URL_SEARCH_SECOND_TRIA = 'https://www.phptravels.net/hotels/detail/istanbul/tria-hotel-istanbul-special/29-12-2020/31-12-2020/0/0'
    URL_SEARCH_THIRD_TRIA = 'https://www.phptravels.net/hotels/detail/istanbul/tria-hotel-istanbul-special/30-12-2020/29-12-2020/2/2'
    PAGE_TITLE_SEARCH_DEFAULT_TRIA = 'Tria Hotel Istanbul Special'

    # Element Locators
    HOTEL_TITLE = (By.XPATH, "//h2[@id='detail-content-sticky-nav-00']")

    # Methods
    def load_page_result_first_tria(self):
        self.browser.get(self.URL_SEARCH_FIRST_TRIA)

    def load_page_result_second_tria(self):
        self.browser.get(self.URL_SEARCH_SECOND_TRIA)

    def load_page_result_third_tria(self):
        self.browser.get(self.URL_SEARCH_THIRD_TRIA)

    def verify_title_result_tria(self):
        assert self.browser.title == self.PAGE_TITLE_SEARCH_DEFAULT_TRIA

    def verify_url_result_first_tria(self):
        assert self.browser.current_url == self.URL_SEARCH_FIRST_TRIA

    def verify_url_result_second_tria(self):
        assert self.browser.current_url == self.URL_SEARCH_SECOND_TRIA

    def verify_url_result_third_tria(self):
        assert self.browser.current_url == self.URL_SEARCH_THIRD_TRIA