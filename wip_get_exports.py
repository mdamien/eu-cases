from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os.path

os.makedirs('export', exist_ok=True)

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.path.join(os.getcwd(), 'export'))
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
    "application/vnd.ms-excel")

driver = webdriver.Firefox(fp)


def do(type):
    driver.get("http://ec.europa.eu/competition/elojade/isef/index.cfm")
    driver.find_element_by_css_selector('.classRadioButton{} input'.format(type)).click()
    driver.find_element_by_css_selector('.submit').click()
    driver.find_element_by_css_selector('input[value="Export"]').click()

do('ATC')
do('M')
do('SA')

# poll to know if download is finished and close selenium