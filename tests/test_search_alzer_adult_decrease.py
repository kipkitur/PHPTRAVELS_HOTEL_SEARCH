import pytest
from pages.home_page_alzer import PhpTravelsHomePageAlzer
from pages.search_result_alzer import PhpTravelsSearchResultPageAlzer


@pytest.mark.parametrize("hotel_alzer, checkin_alzer, checkout_alzer", [
    ("Alzer Hotel Istanbul, Istanbul", "10/29/2020", "10/31/2020"),
    ("Alzer Hotel Istanbul, Istanbul", "12/29/2019", "12/31/2019"),
    ("Alzer Hotel Istanbul, Istanbul", "12/30/2020", "12/29/2020")
])

@pytest.mark.hotelsearch
def test_search_alzer(browser, hotel_alzer, checkin_alzer, checkout_alzer):
    home_page = PhpTravelsHomePageAlzer(browser)
    search_result_page = PhpTravelsSearchResultPageAlzer(browser)

    # navigate to PhpTravels home page
    home_page.load_page()

    # Verify title and current url
    home_page.verify_title()
    home_page.verify_url()

    # search for hotel
    home_page.enter_alzer_details_adult_decrease(hotel_alzer, checkin_alzer, checkout_alzer)

    # click on search button
    home_page.click_search_button()

    # search result page
    search_result_page.load_page_result()
    search_result_page.verify_title_result()
    search_result_page.verify_url_result_second()

