from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os.path

os.makedirs('list_pages', exist_ok=True)

driver = webdriver.Firefox()
driver.get("http://ec.europa.eu/competition/elojade/isef/index.cfm")
driver.find_element_by_css_selector('.submit').click()

i = 0
while True:
    print(i)
    filename = 'list_pages/%d.html' % i
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(driver.page_source)
    driver.find_element_by_css_selector('input[value="Next"]').click()
    i += 1

driver.close()
