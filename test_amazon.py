import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

signInField = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@id ='nav-link-accountList']")))
signInField.click()

userNameField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_email")))
userNameField.clear()
userNameField.send_keys("testamazon117@gmail.com")
userNameField.send_keys(Keys.ENTER)

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_password")))
password.send_keys("123456")
time.sleep(3)
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.quit()