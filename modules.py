# All the header files needed by the tests
# And opening the website

from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep
# Set options for not prompting DevTools information

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])
from selenium.webdriver.chrome.options import Options as ChromeOptions

driver = webdriver.Chrome(options=options)


### When using SauceLabs for visualization and analysis of the tests
# options = ChromeOptions()
# options.browser_version = '112'
# options.platform_name = 'Windows 10'
# sauce_options = {}
# sauce_options['build'] = 'selenium-build-KB80I'
# sauce_options['name'] = 'test_5'
# options.set_capability('sauce:options', sauce_options)

# url = "https://oauth-syedjawadakhtar-**************@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
# driver = webdriver.Remote(command_executor=url, options=options)

# Visiting Profilences.com
driver.get("https://profilence.com/")

# Waiting to load the site completely
sleep(3)