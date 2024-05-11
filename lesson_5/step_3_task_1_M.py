from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for i in range(5):
    addElButton = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

numDelButton = driver.find_elements(By.CSS_SELECTOR, "[class='added-manually']")
print(len(numDelButton))

sleep(10)
driver.quit()
