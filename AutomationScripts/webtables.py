from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")
print("Website opened")

wait = WebDriverWait(driver, 10)

# Open Elements
elements = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
driver.execute_script("arguments[0].click();", elements)

# Open Web Tables
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))
).click()

print("Web Tables opened")

# ADD RECORD
wait.until(
    EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
).click()

driver.find_element(By.ID, "firstName").send_keys("Ali")
driver.find_element(By.ID, "lastName").send_keys("Khan")
driver.find_element(By.ID, "userEmail").send_keys("ali@test.com")
driver.find_element(By.ID, "age").send_keys("25")
driver.find_element(By.ID, "salary").send_keys("50000")
driver.find_element(By.ID, "department").send_keys("QA")

driver.find_element(By.ID, "submit").click()

print("Record Added")

# EDIT RECORD
edit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@id='edit-record-4']"))
)
edit_btn.click()

name_field = driver.find_element(By.ID, "firstName")
name_field.clear()
name_field.send_keys("Ali Updated")

driver.find_element(By.ID, "submit").click()

print("Record Edited")

# DELETE RECORD
delete_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@id='delete-record-4']"))
)
delete_btn.click()

print("Record Deleted")

# VERIFY (basic check)
rows = driver.find_elements(By.XPATH, "//div[@role='rowgroup']")

if len(rows) > 0:
    print("Table exists - PASS")
else:
    print("Table empty - CHECK")

input("Press Enter to close...")
driver.quit()