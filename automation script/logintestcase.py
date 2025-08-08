from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create service object
serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")

# Launch Chrome browser
driver = webdriver.Chrome(service=serv_obj)

# Open the URL (corrected the typo in URL)
driver.get("https://opensource-demo.orangehrmlive.com/")

# Locate and fill username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Locate and fill password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Click login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Get actual title
act_title = driver.title
exp_title = "OrangeHRM"

# Compare titles
if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

# Close browser
driver.close()
