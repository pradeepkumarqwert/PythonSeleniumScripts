from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

caps = {
    "deviceName": "Vivo V40 Pro",
    "platformName": "Android",
    "platformVersion": "14",
    "app": "General-Store-final (1).apk"
}

server_url = "https://cloud.fireflink.com/backend/fireflinkcloud/wd/hub?accessKey=aeedf5e8-d698-4876-9ab0-aeab6a084b86&licenseId=LIC1026493&projectName=Project+for+Demo/"

driver = webdriver.Remote(server_url, caps)
wait = WebDriverWait(driver, 20)

def take_screenshot(name):
    path = f"C:\\SimpleRunScreenshots\\{name}.png"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")

try:
    # Select country
    country_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Spinner[@resource-id='com.androidsample.generalstore:id/spinnerCountry']")))
    country_dropdown.click()
    take_screenshot("01_CountryDropdown_Click")
    time.sleep(1)

    country_option = driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='android:id/text1' and @text='Afghanistan']")
    country_option.click()
    take_screenshot("02_Country_Selected")

    # Enter name
    name_field = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='com.androidsample.generalstore:id/nameField']")
    name_field.send_keys("Tester1")
    take_screenshot("03_Name_Entered")
    driver.hide_keyboard()

    # Select gender
    driver.find_element(By.XPATH, "//android.widget.RadioButton[@resource-id='com.androidsample.generalstore:id/radioMale']").click()
    take_screenshot("04_Gender_Selected")

    # Click Lets Shop
    driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='com.androidsample.generalstore:id/btnLetsShop']").click()
    take_screenshot("05_LetsShop_Clicked")
    time.sleep(2)

    # Add product to cart
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='Air Jordan 4 Retro']/following-sibling::android.widget.LinearLayout//android.widget.TextView[@resource-id='com.androidsample.generalstore:id/productAddCart']").click()
    take_screenshot("06_Product_Added")
    time.sleep(1)

    # Open Cart
    driver.find_element(By.XPATH, "//android.widget.ImageButton[@resource-id='com.androidsample.generalstore:id/appbar_btn_cart']").click()
    take_screenshot("07_Cart_Page")

    print("Test execution completed successfully.")

except Exception as e:
    print("Exception occurred:", e)
    take_screenshot("99_Exception")
finally:
    driver.quit()
