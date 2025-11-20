from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

caps = {
    "deviceName": "iPhone 14",
    "platformName": "iOS",
    "platformVersion": "18.5",
    "browserName": "Safari"
}

server_url = ""

driver = webdriver.Remote(server_url, caps)
wait = WebDriverWait(driver, 15)

def take_screenshot(name):
    path = f"C:\\SimpleRunScreenshots\\{name}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")

try:
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)
    search_input = wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
    search_input.send_keys("iPhone")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))

    print("Title after search:", driver.title)

    # Scroll
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)

    # Click first Apple link
    link = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href,'Apple')])[1]")))
    link.click()
    time.sleep(2)

    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    print("Opened page:", heading.text)

    driver.back()
    time.sleep(2)
    print("Now on:", driver.current_url)

    driver.refresh()
    time.sleep(2)

except Exception as e:
    print("Exception occurred:", e)
    take_screenshot("99_Exception_Occurred")
finally:
    driver.quit()
