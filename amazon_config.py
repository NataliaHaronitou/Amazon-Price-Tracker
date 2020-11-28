from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'rtx 3080'
CURRENCY = '$'
MIN_PRICE = '100'
MAX_PRICE = '8000'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
    }

BASE_URL = "http://www.amazon.com/"

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver', chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

# Found on the code below on stackoverflow; sometimes its best to get things done the fastest way possible 

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')




