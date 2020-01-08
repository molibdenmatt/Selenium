import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")

checkbox.click()

if checkbox.is_selected():
    print("Checkbox selected! Revert!")
    checkbox.click()
else:
    print("Checkbox not selected! Selecting!")
    checkbox.click()

driver.quit()

