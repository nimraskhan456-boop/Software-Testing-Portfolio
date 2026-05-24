# import time
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://demoqa.com")

# time.sleep(10)  # 10 sec wait

# driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()

# driver.get("https://demoqa.com")

# print("Website opened")

# wait = WebDriverWait(driver, 10)

# forms = wait.until(
#     EC.presence_of_element_located((By.XPATH, "//h5[text()='Forms']"))
# )

# # scroll into view (IMPORTANT)
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", forms)

# time.sleep(1)

# # now click
# wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']"))).click()

# print("Forms clicked")

# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# fix encoding issue
sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com")
print("Website opened")

wait = WebDriverWait(driver, 10)

forms = wait.until(
    EC.presence_of_element_located((By.XPATH, "//h5[text()='Forms']"))
)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", forms)
time.sleep(1)

driver.execute_script("arguments[0].click();", forms)
print("Forms clicked")

time.sleep(2)

inputs = driver.find_elements(By.TAG_NAME, "input")

if len(inputs) == 0:
    print("No editable input field found (Only UI elements present)")
else:
    print("Input elements exist (UI check needed)")

input("Press Enter to close browser...")

driver.quit()