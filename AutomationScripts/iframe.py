from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com")
print("Website opened")

# =========================
# ALERTS SECTION
# =========================

# Open Alerts, Frame & Windows
section = wait.until(
    EC.presence_of_element_located((By.XPATH, "//h5[text()='Alerts, Frame & Windows']"))
)

driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)
driver.execute_script("arguments[0].click();", section)

print("Alerts section opened")

# Open Alerts page
alerts = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Alerts']"))
)
driver.execute_script("arguments[0].click();", alerts)

print("Alerts page opened")

# Click Alert Button (FIXED)
alert_btn = wait.until(
    EC.presence_of_element_located((By.ID, "alertButton"))
)

driver.execute_script("arguments[0].scrollIntoView({block:'center'});", alert_btn)
driver.execute_script("arguments[0].click();", alert_btn)

# Handle alert popup
alert = wait.until(EC.alert_is_present())
print("Alert text:", alert.text)
alert.accept()

print("Alert handled successfully")

# =========================
# IFRAME SECTION
# =========================

driver.get("https://demoqa.com/frames")
print("Frames page opened")

# Switch to iframe
wait.until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
)

frame_text = wait.until(
    EC.presence_of_element_located((By.ID, "sampleHeading"))
).text

print("Iframe text:", frame_text)

# Back to main page
driver.switch_to.default_content()

print("Switched back from iframe")

# =========================
# DONE
# =========================

print("Automation completed successfully - PASS")

input("Press Enter to close...")
driver.quit()