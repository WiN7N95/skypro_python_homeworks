from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for i in range(5):
    AddElButton = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()

NumDelButton = driver.find_elements(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
print(len(NumDelButton))

sleep(10)
driver.quit()