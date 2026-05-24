from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("START")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")
print("Website opened")

wait = WebDriverWait(driver, 10)

# Click Elements
elements = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
elements.click()

# Click Radio Button
radio = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Radio Button']"))
)
radio.click()

print("Radio Button page opened")

time.sleep(2)

# Select Yes
yes = driver.find_element(By.XPATH, "//label[text()='Yes']")
yes.click()

time.sleep(1)

# Verify output
output = driver.find_element(By.CLASS_NAME, "mt-3").text

if "Yes" in output:
    print("TEST PASS  Yes selected successfully")
else:
    print("TEST FAIL ")

input("Press Enter to close...")
driver.quit()