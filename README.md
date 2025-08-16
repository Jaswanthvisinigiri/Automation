# Automation

Selenium Login Automation with Python
A simple Selenium automation project in Python that launches Chrome, navigates to OrangeHRM demo, logs in, and verifies the page title. Designed as a learning starter for test automation.

**Table of Contents**
* Overview
* Setup & Installation
* How it Works
* Technologies Used


  **Overview**
* This project demonstrates how to:
* Launch Chrome browser using Selenium WebDriver
* Navigate to OrangeHRM demo site
* Input credentials and perform login actions
* Validate the page title to confirm successful login
* Close the browser session gracefully

A great hands-on example to get familiar with web automation workflows.

**Setup & Installation
**Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/selenium-login-demo.git
cd selenium-login-demo
Install dependencies
Using virtual environment is recommended:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install selenium
Download ChromeDriver
Download the version matching your Chrome browser and place it in a known directory (e.g., C:\Drivers\chromedriver.exe). Update the path in your script if needed.

**How it Works:******

1.The script workflow:
2.Initializes Chrome WebDriver with a specified driver path
3.Opens OrangeHRM demo login page
4.Enters username = Admin and password = admin123
5.Clicks the login button
6.Checks the page title against expected value "OrangeHRM"
7.Prints a success or failure message
8.Closes the browser instance gracefully
This approach validates successful login by confirming the page title, a simple yet effective method.

**Technologies Used**
Technology	         Purpose
Python 3	             Programming language
Selenium WebDriver	   Browser automation framework
Chrome WebDriver	     Controls the Chrome browser

**personal details if you have any douts:**
contact:8985957264
mailID:jaswanthv2004@gmail.com





