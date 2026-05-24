from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("START")

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/books")
print("Book Store page opened")

wait = WebDriverWait(driver, 30)

# 🔥 wait for table container first (important)
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "rt-table"))
)

# small buffer for React render
time.sleep(3)

# 🔥 correct book title selector (stable one)
books = driver.find_elements(By.XPATH, "//div[@class='rt-td']/a")

print("Book titles found:", len(books))

if len(books) == 8:
    print("Books displayed correctly - PASS")
else:
    print("Mismatch detected - Found:", len(books), "Expected: 8")

input("Press Enter to close...")
driver.quit()