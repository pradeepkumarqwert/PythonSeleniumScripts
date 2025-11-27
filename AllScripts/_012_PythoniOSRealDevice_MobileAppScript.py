from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# --------------------------
# FireFlink Hub URL
options = XCUITestOptions()
options.device_name = "iPhone 11"
options.platform_name = "iOS"
options.platform_version = "18.3.1"
options.app = "bigbasket.ipa"
options.bundle_id = "com.bigbasket.mobileapp"
options.automation_name = "XCUITest"
device_farm_hub_url = "https://fireflinkclouddev.fireflink.com/backend/fireflinkcloud/wd/hub?accessKey=357782b4-a55a-46a3-9eef-4d0e3db10941&licenseId=LIC4743&projectName=TestingCaps"

# Use 'desired_capabilities' here
driver = webdriver.Remote(command_executor=device_farm_hub_url, options=options)
act = ActionChains(driver)

try:
    # --------------------------
    # Tap at coordinates (271, 520)
    # --------------------------
    act.move_by_offset(271, 520).click().perform()
    time.sleep(1)

    # --------------------------
    # Continue as Guest
    # --------------------------
    driver.find_element(By.XPATH, "//XCUIElementTypeStaticText[@name='Continue as Guest']").click()
    time.sleep(1)

    # --------------------------
    # Click Categories
    # --------------------------
    try:
        driver.find_element(By.XPATH,
            "//XCUIElementTypeStaticText[@name='Home']/following::XCUIElementTypeStaticText[@value='Categories']"
        ).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//XCUIElementTypeStaticText[@name='Categories']").click()

    # --------------------------
    # Select Breakfast Category
    # --------------------------
    driver.find_element(By.XPATH,
        "//XCUIElementTypeStaticText[@name='Categories']/following::XCUIElementTypeStaticText[contains(@name,'Breakfast')][2]"
    ).click()

    # --------------------------
    # Click first offer tag & add product
    # --------------------------
    driver.find_element(By.XPATH,
        "//XCUIElementTypeStaticText[@value='All']/following::XCUIElementTypeOther[@name='offerTag'][1]"
    ).click()
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='addButtonProduct']").click()

    # --------------------------
    # Click on specific coordinates
    # --------------------------
    act.move_by_offset(344, 747).click().perform()

    # --------------------------
    # Decrement product
    # --------------------------
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='decrementProductButton']").click()

    # --------------------------
    # Navigate back twice
    # --------------------------
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='backButton']").click()
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='backButton']").click()

    # --------------------------
    # Select Flakes category
    # --------------------------
    driver.find_element(By.XPATH,
        "//XCUIElementTypeStaticText[@name='Breakfast Cereals']/following::XCUIElementTypeStaticText[@name='Flakes']"
    ).click()

    # --------------------------
    # Repeat offer and add product
    # --------------------------
    driver.find_element(By.XPATH,
        "//XCUIElementTypeStaticText[@value='All']/following::XCUIElementTypeOther[@name='offerTag'][1]"
    ).click()
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='addButtonProduct']").click()
    act.move_by_offset(344, 747).click().perform()
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='decrementProductButton']").click()

    # Navigate back
    driver.find_element(By.XPATH, "//XCUIElementTypeButton[@name='backButton']").click()

except Exception as e:
    print("Exception occurred:", e)

finally:
    if driver:
        driver.quit()
    else:
        print("Driver not initialized. Session creation failed.")
