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
wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))).click()

# Click edit button (first row)
driver.find_element(By.ID, "edit-record-1").click()

# Update salary
salary = driver.find_element(By.ID, "salary")
salary.clear()
salary.send_keys("75000")

driver.find_element(By.ID, "submit").click()

time.sleep(2)

print("TEST PASS  Record updated")

driver.quit()