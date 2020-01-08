import os
import time
from selenium import webdriver
import selenium.webdriver.common.by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")
driver.maximize_window()

paragraph_visible = driver.find_element_by_tag_name("p")
if paragraph_visible.is_displayed():
    print(paragraph_visible.text)
else:
    print("Element not visible")
    print(paragraph_visible.get_attribute("textContent"))

time.sleep(3)
driver.quit()
