from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create service object
serv_obj = Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")

# Launch Chrome browser
driver = webdriver.Chrome(service=serv_obj)

# Open the site
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Search for "laptop"
driver.find_element(By.ID, "small-searchterms").send_keys("laptop")

# Click the "Register" link
driver.find_element(By.LINK_TEXT, "Register").click()

# Close browser
driver.close()
