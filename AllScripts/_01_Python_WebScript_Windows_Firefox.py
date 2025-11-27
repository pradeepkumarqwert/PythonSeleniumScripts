import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def take_screenshot(driver, file_name):
    folder = r"C:\SimpleRunScreenshots"
    os.makedirs(folder, exist_ok=True)
    driver.save_screenshot(os.path.join(folder, file_name + ".png"))


def main():

    driver = None

    try:

        device_farm_hub_url = 'https://fireflinkclouddev.fireflink.com/backend/fireflinkcloud/wd/hub?accessKey=357782b4-a55a-46a3-9eef-4d0e3db10941&licenseId=LIC4743&projectName=TestingCaps'
        options = webdriver.FirefoxOptions()
        options._caps = {}
        options.set_capability("browserName", "firefox")
        options.set_capability("platformName", "Windows 11")
        options.set_capability("browserVersion", "134")

        driver = webdriver.Remote(
            command_executor=device_farm_hub_url,
            options=options
        )

        driver.set_window_size(1024, 768)



        device_farm_hub_url = "https://fireflinkclouddev.fireflink.com/backend/fireflinkcloud/wd/hub?accessKey=xnZJRvKL6F26IuCM3K3pe-oSuykml-D0u6GrTaLLwdaPk9OS80lI6mGP2fYdYGwVuP5kaDO_zcElBor3m_lh2fgDWT7n0MBXfWZ6PBZyKaIdbyyUv-Fymw7NaySl4XENMPmgOpt2z-gR0RrH0gZvuV2JukC_19mVB3sawJ__i-AibN9y9Ae4QmD3P4qcDqbRYln_OMFy6ckvhuRPr6KkACpdUsfm4NsTq1ddoOYxd9RTEfydGwkcDX8GuyAaGtYIm_z6sHUjynycvlhuCbZnNV30Fg9Yp4JidXKK5sIkWQ&licenseId=LIC4639&projectName=Project-03";
        options = webdriver.ChromeOptions()
        options.set_capability('platformName', 'Windows 10')
        options.set_capability('browserVersion', '134')
        driver = webdriver.Remote(device_farm_hub_url, options=options)
        driver.set_window_size(1024, 768)





        driver.get("https://www.google.com")
        take_screenshot(driver, "01_Google_Page")

        driver.get("https://www.pantaloons.com")
        take_screenshot(driver, "02_Pantaloons_Landing")

    except Exception as e:
        print("Error:", e)

    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
