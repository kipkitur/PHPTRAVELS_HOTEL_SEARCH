"""
This module contains page object for PhpTravel home page.
Limited to Hotels functionality only.
Automates Tria Hotel Istanbul search functionality.
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PhpTravelsHomePageTria:

    # Initializer
    # use the init method to crate attributes that are members of a class
    # the self argument makes sure the attribute is available to other class methods
    def __init__(self, browser):
        self.browser = browser

    # URL and page title
    URL = 'https://www.phptravels.net/home'
    PAGE_TITLE = 'PHPTRAVELS | Travel Technology Partner'

    # Element Locators
    HOTELS_BUTTON = (By.LINK_TEXT, "Hotels")
    DESTINATION_INPUT = (By.XPATH, "//form[@name='HOTELS']//div[@class='form-icon-left typeahead__container']")
    TRIA = (By.XPATH, "//div[.='Tria Hotel Istanbul Especial, Istanbul']")
    CHECKIN_DATE = (By.ID, "checkin")
    CHECKOUT_DATE = (By.ID, "checkout")
    ADULT_COUNT_DECREASE = (By.XPATH, "//div[contains(@class,'col o2')]//button[contains(text(), '-')]")
    ADULT_COUNT_INCREASE = (By.XPATH, "//div[contains(@class,'col o2')]//button[contains(text(), '+')]")
    CHILD_COUNT_DECREASE = (By.XPATH, "//div[contains(@class,'col 01')]//button[contains(text(),'-')]")
    CHILD_COUNT_INCREASE = (By.XPATH, "//div[contains(@class,'col 01')]//button[contains(text(),'+')]")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Search')]")

    # Methods
    # load the page
    def load_page(self):
        self.browser.get(self.URL)
    # compare current title with page title
    def verify_title(self):
        assert self.browser.title == self.PAGE_TITLE
    # verify current URL against current page URL
    def verify_url(self):
        assert self.browser.current_url == self.URL

    # 2 adults 0 children
    def enter_tria_details(self, hotel_name, checkin_date, checkout_date):
        destination_input_field = self.browser.find_element(*self.DESTINATION_INPUT)
        destination_input_field.click()
        hotel = self.browser.find_element(*self.TRIA)
        hotel.click()
        checkin = self.browser.find_element(*self.CHECKIN_DATE)
        checkin.clear()
        checkin.send_keys(checkin_date)
        checkout = self.browser.find_element(*self.CHECKOUT_DATE)
        checkout.clear()
        checkout.send_keys(checkout_date)


    # 2 adults 2 children
    def enter_tria_details_children_increase(self, hotel_name, checkin_date, checkout_date):
        destination_input_field = self.browser.find_element(*self.DESTINATION_INPUT)
        destination_input_field.click()
        hotel = self.browser.find_element(*self.TRIA)
        hotel.click()
        checkin = self.browser.find_element(*self.CHECKIN_DATE)
        checkin.clear()
        checkin.send_keys(checkin_date)
        checkout = self.browser.find_element(*self.CHECKOUT_DATE)
        checkout.clear()
        checkout.send_keys(checkout_date)
        children = self.browser.find_element(*self.CHILD_COUNT_INCREASE)
        action = ActionChains(self.browser)
        action.double_click(on_element= children)
        action.perform()


    # 0 adults 0 children
    def enter_tria_details_adult_decrease(self, hotel_name, checkin_date, checkout_date):
        destination_input_field = self.browser.find_element(*self.DESTINATION_INPUT)
        destination_input_field.click()
        hotel = self.browser.find_element(*self.TRIA)
        hotel.click()
        checkin = self.browser.find_element(*self.CHECKIN_DATE)
        checkin.clear()
        checkin.send_keys(checkin_date)
        checkout = self.browser.find_element(*self.CHECKOUT_DATE)
        checkout.clear()
        checkout.send_keys(checkout_date)
        adult = self.browser.find_element(*self.ADULT_COUNT_DECREASE)
        action = ActionChains(self.browser)
        action.double_click(on_element=adult)
        action.perform()

    # find the search button element and click on it.
    def click_search_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()



