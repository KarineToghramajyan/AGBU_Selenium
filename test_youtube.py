import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("adele")
time.sleep(3)
search_box.send_keys(Keys.ENTER)
time.sleep(3)

first_video = driver.find_element(By.XPATH, "//ytd-video-renderer")
first_video.click()
time.sleep(15)

pause_button = driver.find_element(By.CLASS_NAME, "ytp-play-button.ytp-button")
pause_button.click()
time.sleep(5)

driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("adele")
time.sleep(3)
search_box.send_keys(Keys.ENTER)
time.sleep(3)

second_video = driver.find_element(By.XPATH, "//ytd-video-renderer[2]")
# class="style-scope ytd-video-preview">
second_video.click()
time.sleep(15)

pause_button = driver.find_element(By.CLASS_NAME, "ytp-play-button.ytp-button")
pause_button.click()
time.sleep(5)

driver.quit()