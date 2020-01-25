import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome


@pytest.fixture()  # Fixture describes what will happen before and after the actual method
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Manage drivers with webdriver_manager
    cwd = os.getcwd()
    driver.get("file:///Users/mateuszswieton/private_stuff/Selenium/Selenium/test_sites/Test.html")
    driver.maximize_window()
    yield
    driver.quit()  # Will work after out test method


def test_page_title(test_setup):
    assert driver.title == "Strona testowa", "Wrong page open"


def test_page_title2(test_setup):
    assert driver.find_element_by_tag_name("h1").text == "Witaj na stronie testowej", "Wrong page open"
