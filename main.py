from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeDriver = "D:\\scripts\\chromedriver.exe"

option = webdriver.ChromeOptions()

option.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

option.add_experimental_option("detach", True)

s = Service(chromeDriver)

driver = webdriver.Chrome(service=s, options=option)

driver.maximize_window()

driver.get("https://google.com/")

driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("Rahul Jha SoftoCorp")

driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Keys.ENTER)

