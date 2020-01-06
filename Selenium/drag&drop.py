import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()
time.sleep(3)
element_to_drag = driver.find_element_by_id("draggable")
drag_target = driver.find_element_by_id("droptarget")
webdriver.ActionChains(driver).drag_and_drop(element_to_drag, drag_target).perform()


time.sleep(6)
driver.quit()