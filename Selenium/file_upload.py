import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
cwd = os.getcwd()  # Current working directory
driver.get("file://" + cwd + "/test_sites/FileUpload.html")


upload_button = driver.find_element_by_id("myFile")
upload_file = cwd + "/test_sites/uploadMe.txt"
upload_button.send_keys(upload_file)


driver.quit()