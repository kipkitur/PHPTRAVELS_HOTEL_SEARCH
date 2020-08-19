import pytest
from pages.home_page_tria import PhpTravelsHomePageTria
from pages.search_result_tria import PhpTravelsSearchResultPageTria


@pytest.mark.parametrize("hotel_tria, checkin_tria, checkout_tria", [
    ("Tria Hotel Istanbul Especial, Istanbul", "10/29/2020", "10/31/2020"),
    ("Tria Hotel Istanbul Especial, Istanbul", "12/29/2019", "12/31/2019"),
    ("Tria Hotel Istanbul Especial, Istanbul", "12/30/2020", "12/29/2020")
])

@pytest.mark.regressiontest
def test_search_tria(browser, hotel_tria, checkin_tria, checkout_tria):
    home_page = PhpTravelsHomePageTria(browser)
    # search_result_page = PhpTravelsSearchResultPage(browser)

    # navigate to PhpTravels home page
    home_page.load_page()

    # Verify title and current url
    home_page.verify_title()
    home_page.verify_url()

    # search for hotel - 2 adults 0 children
    home_page.enter_tria_details_adult_decrease(hotel_tria, checkin_tria, checkout_tria)

    # click on search button
    home_page.click_search_button()