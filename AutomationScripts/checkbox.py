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

# Click Check Box
checkbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Check Box']"))
)
checkbox.click()

print("Check Box page opened")

time.sleep(2)

# Expand Home
home = driver.find_element(By.XPATH, "//button[@title='Toggle']")
home.click()

time.sleep(1)

# Select Desktop
desktop = driver.find_element(By.XPATH, "//span[text()='Desktop']")
desktop.click()

time.sleep(1)

# Select Notes
notes = driver.find_element(By.XPATH, "//span[text()='Notes']")
notes.click()

time.sleep(2)

# Verify output
output = driver.find_element(By.ID, "result").text

if "desktop" in output.lower():
    print("TEST PASS ✔️ Check Box working correctly")
else:
    print("TEST FAIL ❌")

input("Press Enter to close...")
driver.quit()