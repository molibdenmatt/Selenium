import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/iFrameTest.html")
driver.maximize_window()

print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
print(driver.find_element_by_tag_name("h1").text)
driver.switch_to.default_content()


time.sleep(3)
driver.quit()

