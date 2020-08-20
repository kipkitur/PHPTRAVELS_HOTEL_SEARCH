import platform
import pytest
from selenium import webdriver

resources_location = "../resources/chromedriver_win_{}.exe"
exception_message = "chromedriver is not configured for your Operation System! Your Operating System is: {}"

@pytest.fixture()
def browser():
    chrome_version_win = "84"
    chrome_version_mac = "84"

    if 'Win' in platform.platform():
        browser = webdriver.Chrome(resources_location.format(chrome_version_win))
    elif 'darwin' in platform.platform():
        browser = webdriver.Chrome(resources_location.format(chrome_version_mac))
    elif 'macOS' in platform.platform():
        browser = webdriver.Chrome(resources_location.format(chrome_version_mac))
    else:
        raise Exception(exception_message.format(platform.platform()))

    # wait 10 seconds to pull the DOM
    browser.implicitly_wait(10)
    # maximize browser window to full screen
    browser.maximize_window()
    yield browser
    # when test is done, close ALL windows of the browser
    browser.quit()
