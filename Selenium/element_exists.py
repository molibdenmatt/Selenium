import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")

magic_element = driver.find_elements_by_tag_name("papa")

# list length method
if len(magic_element) > 0:
    print("Element actually does exist")
else:
    print("No such element found")

# try/except method
try:
    driver.find_element_by_tag_name("papa")
    print("Element does exist")
except NoSuchElementException:
    print("No such element found")

driver.quit()
