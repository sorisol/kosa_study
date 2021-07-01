import time
from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument("user-agent=Mozilla/5.0")
#options.add_argument("--start-maximized")

#driver = webdriver.Chrome('c:/DevTools/chromedriver.exe', chrome_options=options)
driver = webdriver.Chrome('C:\_kosa\chromedriver.exe')

url = "https://www.naver.com/"

driver.get(url)
time.sleep(2)

inputElement = driver.find_element_by_name("query")
inputElement.clear()
time.sleep(1)
inputElement.send_keys("개발자")
time.sleep(1)
inputElement.submit()
time.sleep(1)

results = driver.find_elements_by_class_name('total_tit')
time.sleep(1)
for one in results:
	print(one.text)
time.sleep(1)

results[0].click()
time.sleep(2)


# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()
