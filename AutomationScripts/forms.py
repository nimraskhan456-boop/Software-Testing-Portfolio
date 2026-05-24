from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")
print("Website opened")

wait = WebDriverWait(driver, 10)

# Scroll
driver.execute_script("window.scrollBy(0, 500);")

# Open Forms
forms = wait.until(
    EC.presence_of_element_located((By.XPATH, "//h5[text()='Forms']"))
)
driver.execute_script("arguments[0].click();", forms)

# Open Practice Form
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']"))
).click()

print("Form opened")

# Fill basic details
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Ali")
driver.find_element(By.ID, "lastName").send_keys("Khan")
driver.find_element(By.ID, "userEmail").send_keys("ali@test.com")

# Gender
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Mobile
driver.find_element(By.ID, "userNumber").send_keys("0300123456")

# Date of Birth (simple click, no complex handling)
driver.find_element(By.ID, "dateOfBirthInput").click()

# Subjects
driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
driver.find_element(By.ID, "subjectsInput").send_keys("\n")

# Hobbies
# driver.find_element(By.XPATH, "//label[text()='Sports']").click()
hobby = driver.find_element(By.XPATH, "//label[text()='Sports']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hobby)
driver.execute_script("arguments[0].click();", hobby)

# Address
driver.find_element(By.ID, "currentAddress").send_keys("Test Address Lahore")

# Scroll to dropdowns
driver.execute_script("window.scrollBy(0, 300);")

# State dropdown
driver.find_element(By.ID, "state").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))).click()

# City dropdown
driver.find_element(By.ID, "city").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']"))).click()

print("Form filled successfully")

# Submit
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
submit.click()

# Verify
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

print("Form submitted - PASS")

input("Press Enter to close...")
driver.quit()