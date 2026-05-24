from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")
print("Website opened")

wait = WebDriverWait(driver, 10)

# 1. Click Elements
elements = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
elements.click()
print("Elements opened")

# 2. Click Text Box
textbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']"))
)
textbox.click()
print("Text Box opened")

# 3. Fill form
driver.find_element(By.ID, "userName").send_keys("Ali Ahmed")
driver.find_element(By.ID, "userEmail").send_keys("ali@test.com")
driver.find_element(By.ID, "currentAddress").send_keys("Rawalpindi, Pakistan")
driver.find_element(By.ID, "permanentAddress").send_keys("Same as above")

print("Form filled")

# 4. Submit
driver.find_element(By.ID, "submit").click()
print("Form submitted")

time.sleep(2)

# 5. Verify output
output = driver.find_element(By.ID, "output").text

if "Ali Ahmed" in output:
    print("TEST PASS  Data saved correctly")
else:
    print("TEST FAIL  Output mismatch")

input("Press Enter to close...")
driver.quit()