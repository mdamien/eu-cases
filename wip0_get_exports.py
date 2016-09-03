import os.path
import shutil

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# clean dir
shutil.rmtree('export', ignore_errors=True)
os.makedirs('export', exist_ok=True)

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.path.join(os.getcwd(), 'export'))
fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
    "application/vnd.ms-excel")

driver = webdriver.Firefox(fp)


def do(type, start_year=None, end_year=None):
    driver.get("http://ec.europa.eu/competition/elojade/isef/index.cfm")
    driver.find_element_by_css_selector('.classRadioButton{} input'.format(type)).click()
    if start_year:
        input = driver.find_element_by_css_selector('input[name="decision_date_from"]')
        input.send_keys('1/1/%d' % start_year)
    if end_year:
        input = driver.find_element_by_css_selector('input[name="decision_date_to"]')
        input.send_keys('1/1/%d' % end_year)
    driver.find_element_by_css_selector('.submit').click()
    driver.find_element_by_css_selector('input[value="Export"]').click()

# export work only if a category of case is selected

do('ATC') # antitrust / carters
do('M') # mergers

# too many state aids, export is failing, so I have to do it category by
do('SA', None, 2000)
do('SA', 2000, 2005)
do('SA', 2005, 2010)
do('SA', 2010, 2015)
do('SA', 2015, None)

# TODO: poll to know if downloads are finished and close selenium