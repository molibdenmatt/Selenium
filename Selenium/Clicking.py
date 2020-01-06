import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/DoubleClick.html")
driver.maximize_window()

# Double click
button = driver.find_element_by_id("bottom")
# webdriver.ActionChains(driver).double_click(button).perform()

# Right click
webdriver.ActionChains(driver).context_click(button).perform()

time.sleep(3)
driver.quit()


