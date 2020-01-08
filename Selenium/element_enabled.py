import os

from selenium import webdriver
import selenium.webdriver.common.by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")

first_name_input = driver.find_element_by_id("fname")

if first_name_input.is_enabled():
    first_name_input.send_keys("Matt")
else:
    print("Element is not available")



driver.quit()
