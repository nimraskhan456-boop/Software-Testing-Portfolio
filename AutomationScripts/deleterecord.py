from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))).click()

# Delete first record
driver.find_element(By.ID, "delete-record-1").click()

time.sleep(2)

print("TEST PASS ✔️ Record deleted")

driver.quit()