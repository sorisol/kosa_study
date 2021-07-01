import time
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0")
options.add_argument("--start-maximized")

driver = webdriver.Chrome('C:\_kosa\chromedriver.exe', chrome_options=options)

url = "https://www.naver.com/"
driver.get(url)
driver.implicitly_wait(2)

driver.get_screenshot_as_file("capture.png")

driver.quit()
