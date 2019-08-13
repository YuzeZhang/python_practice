'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_argument('-headless')
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_option)
url = 'http://www.baidu.com/'
#driver.get(url=url)
browser = webdriver.Chrome()
browser.get(url=url)
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.zhihu.com/')
#assert "Python" in browser.title
elem  = browser.find_element_by_id("Popover7-toggle")
elem.send_keys("python")
elem.send_keys(Keys.RETURN)
print(browser.page_source)
