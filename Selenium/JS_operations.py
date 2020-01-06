import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")
driver.maximize_window()
# driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))

wartosc = "Matt"
driver.execute_script("arguments[0].setAttribute('value' , ' " + wartosc + "')", driver.find_element_by_id("fname"))

time.sleep(3)  # Check visually the outcome
driver.quit()