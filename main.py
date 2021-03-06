from selenium import webdriver
import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chromepath = os.environ.get("CHROMEDRIVER_PATH")
bin = os.environ.get("GOOGLE_CHROME_BIN")
path = os.environ.get("PATH")
print(path)
print(chromepath)
print(bin)
ser = Service(chromepath)

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=ser, options=chrome_options)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print("Test PASSED")
driver.close()
