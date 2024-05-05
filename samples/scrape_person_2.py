import os
from linkedin_scraper import Person, actions
from selenium import webdriver
#driver = webdriver.Chrome("./chromedriver")
#webdriver.Chrome("")
driver = webdriver.Chrome()
email = os.getenv("LINKEDIN_USER")
password = os.getenv("LINKEDIN_PASSWORD")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/ethanransberger", driver=driver)
