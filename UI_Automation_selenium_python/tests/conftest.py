import pytest
from selenium import webdriver

from Utilities import Read_configurations


@pytest.fixture()
def setup_teardown(request):
    browser = Read_configurations.read_configure("basic info","browser")
    driver = None
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__('Firefox'):
        driver = webdriver.Firefox()
    elif browser.__eq__('Edge'):
        driver = webdriver.Edge()
    else:
        print("Enter Valid browser name: Chrome/Firefox/Edge")
    driver.maximize_window()
    url = Read_configurations.read_configure("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
