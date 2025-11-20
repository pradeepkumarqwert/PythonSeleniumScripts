from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# --------------------------
# 1. Desired Capabilities
# --------------------------
caps = {
    "deviceName": "Samsung Galaxy A12",
    "platformName": "Android",
    "platformVersion": "12",
    "browserName": "Chrome"
}

# --------------------------
# 2. Appium / Selenium Hub URL
# --------------------------
server_url = ""

driver = webdriver.Remote(server_url, caps)
wait = WebDriverWait(driver, 20)

# --------------------------
# 3. Helper function: Screenshot
# --------------------------
def take_screenshot(name):
    path = f"C:\\SimpleRunScreenshots\\{name}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")

try:
    driver.get("https://www.pantaloons.com/")
    take_screenshot("01_HomePage")
    time.sleep(3)

    # Click search icon
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mobilesearchbox"))).click()
    take_screenshot("02_After_Click_Search_Icon")
    time.sleep(2)

    # Enter "Shirt" in search bar
    search_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search for products,brands and more...']")))
    search_input.send_keys("Shirt")
    take_screenshot("03_After_Entering_Search")
    time.sleep(2)

    # Click first search result
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//mark[text()='Shirt'])[1]"))).click()
    take_screenshot("04_After_Search_Result_Click")
    time.sleep(2)

    # Open Cart
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cartSpriteIcon"))).click()
    take_screenshot("05_Cart_Page")
    print("Page Title:", driver.title)

except Exception as e:
    print("Exception occurred:", e)
    take_screenshot("99_Exception_Occurred")
finally:
    driver.quit()
