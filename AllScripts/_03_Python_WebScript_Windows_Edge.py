import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def take_screenshot(driver, file_name):
    try:
        folder = r"C:\SimpleRunScreenshots"
        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(folder, file_name + ".png")
        driver.save_screenshot(file_path)

        print(f"Screenshot saved: {file_path}")
    except Exception as e:
        print(f"Screenshot failed: {e}")


def main():

    driver = None

    try:
        # ------------------------------------
        # 1. Start Edge browser
        # ------------------------------------


        device_farm_hub_url = 'https://fireflinkclouddev.fireflink.com/backend/fireflinkcloud/wd/hub?accessKey=357782b4-a55a-46a3-9eef-4d0e3db10941&licenseId=LIC4743&projectName=TestingCaps'
        options = webdriver.EdgeOptions()

        options.set_capability('platformName', 'Windows 10')
        options.set_capability('browserVersion', '134')
        driver = webdriver.Remote(command_executor=device_farm_hub_url, options=options)
        driver.set_window_size(1024, 768)

        # ------------------------------------
        # 2. Navigate to Google
        # ------------------------------------
        driver.get("https://www.google.com")
        take_screenshot(driver, "01_Google_Page")

        # ------------------------------------
        # 3. Navigate to Pantaloons website
        # ------------------------------------
        driver.get("https://www.pantaloons.com")
        take_screenshot(driver, "02_Pantaloons_Landing")

        time.sleep(2)

        # ------------------------------------
        # 4. Validate Pantaloons Logo
        # ------------------------------------
        logo = driver.find_element(By.XPATH,
            "//div[@class='nav-header-container']//img[@class='svgIconImg' and @alt='logoIcon']"
        )

        if logo.is_displayed():
            print("Pantaloons logo is displayed")

        take_screenshot(driver, "03_Logo_Visible")

        # ------------------------------------
        # 5. Search for Shirts
        # ------------------------------------
        search_bar = driver.find_element(By.XPATH,
            "//div[@class='nav-links']//input[@placeholder='Search']"
        )

        search_bar.click()
        search_bar.send_keys("Shirts")
        take_screenshot(driver, "04_Typed_Search")

        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        take_screenshot(driver, "05_Search_Results")

        time.sleep(4)

        # ------------------------------------
        # 6. Apply Gender → Boys filter
        # ------------------------------------
        filter_gender = driver.find_element(By.XPATH, "//p[text()='Gender']")
        filter_gender.click()
        take_screenshot(driver, "06_Gender_Filter_Clicked")

        boys_checkbox = driver.find_element(By.XPATH,
            "//p[text()='Boys']//ancestor::div[contains(@class,'PlpWeb_filter-values')]//input"
        )
        boys_checkbox.click()
        take_screenshot(driver, "07_Boys_Filter_Clicked")

        time.sleep(3)

    except Exception as e:
        print("Error: ", e)

    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
