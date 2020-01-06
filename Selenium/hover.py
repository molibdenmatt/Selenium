from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/")
driver.maximize_window()

tutorials_element = driver.find_element_by_id("navbtn_tutorials")
# Chaining actions: hover->click
webdriver.ActionChains(driver).move_to_element(tutorials_element).click(tutorials_element).perform()

driver.quit()
