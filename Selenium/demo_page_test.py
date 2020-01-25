import os
import time

from selenium import webdriver
import selenium.webdriver.common.by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome("drivers/chromedriver") # Manual method
driver = webdriver.Chrome(ChromeDriverManager().install())  # Manage drivers with webdriver_manager

# driver.get("http://www.google.com")
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/Test.html")
driver.set_window_size(1000, 1000)
driver.maximize_window()

# Search by element's ID
driver.find_element(selenium.webdriver.common.by.By.ID, "clickOnMe")
driver.find_element_by_id("clickOnMe")

# Search by element's name
driver.find_element_by_name("fname")
driver.find_element(selenium.webdriver.common.by.By.NAME, "fname")

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

# Xpath selectors
driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
driver.find_element_by_xpath("//tbody//th")
driver.find_element_by_xpath("//th")
driver.find_element_by_xpath("//th[text()='Month']")
driver.find_element_by_xpath("//button[@id='clickOnMe']")
print(driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table").text)

# Find number of elements
num_of_elements = len(driver.find_elements_by_xpath("//th"))
print("Number of th elements on this page: " + str(num_of_elements))

# Interaction with elements - click
driver.find_element_by_id("clickOnMe").click() # Direct method
driver.switch_to.alert.dismiss()
click_me_button = driver.find_element_by_id("clickOnMe")
click_me_button.click()
driver.switch_to.alert.accept()

# Keyboard keys
driver.find_element_by_id("fname").send_keys("Test01234")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
print("You have entered: " + driver.find_element_by_id("fname").get_attribute("value"))

# Clear input
username_input = driver.find_element_by_id("fname")
username_input.clear()

# Select from list
auto_select = Select(driver.find_element_by_tag_name("select"))
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(0)

# Checkbox
driver.find_element_by_xpath("//input[@type='checkbox']").click()

# Radio button
driver.find_element_by_xpath("//input[@value='male']").click()

# Save text from element
radio_text = driver.find_element_by_xpath("//h1").text
print(radio_text)

# Hidden element
print(driver.find_element_by_tag_name("p").get_attribute("textContent"))

# Element size
print(driver.find_element_by_id("smileImage").size.get("height"))  # hardcoded
print(driver.find_element_by_id("smileImage").size.get("naturalHeight"))  # real size(zero if img not loaded)

# Focus on the new window
driver.maximize_window()
driver.find_element_by_id("newPage").click()
print(driver.title)
current_window_name = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)
print("Current window: " + driver.title)

# Screenshot
driver.save_screenshot("screenshots/screen.png")

time.sleep(3)
# driver.close()  # Focused window
driver.quit()  # All windows
