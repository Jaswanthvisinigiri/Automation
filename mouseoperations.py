import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create service object
serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")

# Launch browser
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(3)

# Locate menu elements
admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
usermgmt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

# Mouse hover sequence and click
actions = ActionChains(driver)
actions.move_to_element(admin)\
       .move_to_element(usermgmt)\
       .move_to_element(users)\
       .click()\
       .perform()
