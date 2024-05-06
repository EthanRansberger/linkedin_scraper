import os
from linkedin_scraper import Company, Person, actions
from selenium import webdriver
#driver = webdriver.Chrome("./chromedriver")
#webdriver.Chrome("")E
driver = webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
#email = input("email:")
#password = input("password:")
#email = os.getenv("LINKEDIN_USER")
#password = os.getenv("LINKEDIN_PASSWORD")
email = "ethanransberger@gmail.com"
password = "Eman2020!!!!"

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
#person = Person("https://www.linkedin.com/in/ethanransberger", driver=driver)
company = Company("https://ca.linkedin.com/company/google", driver=driver)
print(company.founded)
company = Company("https://ca.linkedin.com/company/amazon", driver=driver)