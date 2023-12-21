from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_excel(download_path, secret):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)

    # Navigate to the login page
    driver.get("https://liveiq.subway.com/")

    # Wait for the login elements to load and then log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signInName")))
    driver.find_element(By.ID, "signInName").send_keys(secret['username'])
    driver.find_element(By.ID, "password").send_keys(secret['password'])
    driver.find_element(By.ID, "next").click()

    # Wait for the page to load after login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page-title")))

    # Navigate to the Employee Export page
    driver.get("https://liveiq.subway.com/Labour/EmployeeExport")

    # Wait for the export button and click
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "exportEmployees")))
    driver.find_element(By.ID, "exportEmployees").click()

    # Handle the popup if it appears
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="noPayrollNumbers"][@class="white-popup mfp-with-anim"]')))
        driver.find_element(By.ID, "validateOkBtn").click()
    except:
        print("No popup appeared.")

    # Wait for the download to complete
    time.sleep(10)  # Adjust this time based on your network speed and file size

    driver.quit()

# Example usage
secret = {
    "username": "your_username",
    "password": "your_password"
}
download_path = "/path/to/download"
download_excel(download_path, secret)
