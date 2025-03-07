
"""
Simple Selenium in Python - Code Documentation with Real Websites
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Basic Selenium Script
def open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print("Page Title:", driver.title)
    time.sleep(10)
    driver.quit()
    

# 2. Searching on Google
def search_google():
    print("Search executed")
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()
    time.sleep(10)
    driver.quit()

# 3. Logging into GitHub
def login_github():
    print("GitHub login attempted")
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    driver.find_element(By.NAME, "login").send_keys("your_username")
    driver.find_element(By.NAME, "password").send_keys("your_password")
    driver.find_element(By.NAME, "commit").click()
    time.sleep(10)
    driver.quit()
    
    

# 4. Automating Amazon Search
def search_amazon():
    print("Amazon search executed")
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.submit()
    time.sleep(10)
    driver.quit()
   
   
   
"""
 open_google()
  output - Page Title: Google  

  login_github()
    output - GitHub login attempted

  seach_amazon()
    output - Amazon search executed

  search_google()
    output - Search executed
"""

search_amazon()
