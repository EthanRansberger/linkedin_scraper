from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "ethanransberger@gmail.com"
password = "Eman2020!!"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/ethanransberger", driver=driver)