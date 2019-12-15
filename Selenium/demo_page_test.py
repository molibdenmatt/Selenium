from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

# driver = webdriver.Chrome("drivers/chromedriver") # Manual method
driver = webdriver.Chrome(ChromeDriverManager().install())  # Menage drivers with webdriver_manager

# driver.get("http://www.google.com")
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")
driver.set_window_size(1000, 1000)
driver.maximize_window()

# Search by element's ID
driver.find_element(By.ID, "clickOnMe")
driver.find_element_by_id("clickOnMe")

# Search by element's name
driver.find_element_by_name("fname")
driver.find_element(By.NAME, "fname")

# Search by link text
driver.find_element_by_link_text("Visit W3Schools.com!")  # Has to match exactly
driver.find_element_by_partial_link_text("Visit W3Schools.com")  # Has to partially match

# Search by class name
driver.find_element_by_class_name("topSecret")

# Search by tag
driver.find_element_by_tag_name("a")
driver.find_element_by_tag_name("p")
driver.find_element_by_tag_name("label")

# CSS selectors
driver.find_element_by_css_selector("img#smileImage")
driver.find_element_by_css_selector("p.topSecret")
print(driver.find_element_by_css_selector("th:first-child").text)

# .red - all e
# Open new window and close the focused window
# driver.find_element_by_id("newPage").click()
# driver.close()  # Focused window
driver.quit()  # All windows
