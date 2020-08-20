import pytest
from pages.home_page_tria import PhpTravelsHomePageTria


@pytest.mark.smoketest
def test_php_travels_navigation(browser):
    home_page = PhpTravelsHomePageTria(browser)

    # navigate to PhpTravels home page
    home_page.load_page()

    # verify PhpTravels home page title and url
    home_page.verify_title()
    home_page.verify_url()