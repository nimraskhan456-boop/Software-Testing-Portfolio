from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")

wait = WebDriverWait(driver, 10)

# Navigate
wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Alerts, Frame & Windows']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Alerts']"))).click()

# Trigger alert
driver.find_element(By.ID, "alertButton").click()

alert = driver.switch_to.alert
alert.accept()

print("TEST PASS  Alert handled")

driver.quit()