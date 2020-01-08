import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager

# Implicit wait(seconds) - it applies to every find_element_by*
driver.implicitly_wait(10)

cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Waits.html")
driver.maximize_window()

# time library sleep
driver.find_element_by_id('clickOnMe').click()
time.sleep(3)
print(driver.find_element_by_tag_name("p").text)

# Explict wait (max time, poll frequency, ignored issues)
wait = WebDriverWait(driver, 10, 0.5, NoSuchElementException)
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))

# Custom until lambda
wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 1)

# Custom until class
class WaitForListSize:
    def __init__(self, locator, expected_size):
        self.locator = locator
        self.expected_size = expected_size

    def __call__(self, driver):
        return len(driver.find_elements_by_xpath(self.locator)) == self.expected_size


wait.until(WaitForListSize("//p", 1))

driver.quit()
