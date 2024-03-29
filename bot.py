from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from joblib import Parallel, delayed
from config import product_urls
from datetime import datetime
import time
import pickle

def access_sites(product_urls):
    # For concurrent bots
    Parallel(n_jobs=-1)(delayed(initialize_bot)(product_url) for product_url in product_urls)
    print('END OF SCRIPT')

def initialize_bot(product_url): 
    print('item url', product_url)

    # NOTE: THIS TIME IS THE DROP TIME IN EST. PUT THE DROP TIME IN YOUR OWN TIME ZONE.
    #       IN OTHER WORDS, ADJUST THE DROP TIME BY THE TIME DIFFERENCE BETWEEN EST AND 
    #       YOUR OWN TIME ZONE. 
    #       FORMAT: YEAR, MONTH, DAY, HOUR, MINUTE, SECOND
    drop_time = datetime(2019, 10, 31, 13, 31, 1)

    chrome_options = ChromeOptions()
    setChromeOptions(chrome_options)

    # Need to have chromedriver.exe in root directory
    driver = Chrome(options = chrome_options, executable_path='./chromedriver')

    # Wait for elements to appear (in anticipation of high Grailed traffic)
    driver.implicitly_wait(300)

    insert_all_cookies(driver)

    # Sleep until drop time
    seconds_delta = (drop_time - datetime.now()).total_seconds()
    time.sleep(seconds_delta)

    # Begin order execution
    order(product_url, driver, drop_time)

    driver.quit()

def setChromeOptions(chrome_options): 
    # disable loading of images
    prefs = {'profile.managed_default_content_settings.images':2}
    chrome_options.add_experimental_option("prefs", prefs)

    # enable headless
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1980,960")

def order(product_url, driver, drop_time): 
    # Access listing
    driver.get(product_url) 

    # In case item hasn't dropped and link is not updated
    if driver.current_url != product_url:
        print('did not drop yet')
        for i in range(480):
            time.sleep(0.5)
            driver.get(product_url)
            print('i', i)
            if driver.current_url == product_url:
                break

    # PURCHASE
    driver.find_element_by_css_selector('button[title="PURCHASE"]').click()
    
    # CHECKOUT WITH PayPal
    driver.find_element_by_css_selector('button[title="Checkout With PayPal"]').click()
    
    # NOTE: WARNING WARNING WARNING WARNING - YOU WILL PAY:
    pay_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/button')))
    pay_button.click()

    print('Check Grailed/Email to see if you secured it')

def insert_all_cookies(driver):
    insert_cookies('grailed', driver)
    insert_cookies('paypal', driver)

def insert_cookies(website, driver):
    file_name = ''
    url = ''

    if website == 'grailed': 
        file_name = 'cookies_grailed.pkl'
        url = 'https://www.grailed.com/404'
    elif website == 'paypal':
        file_name = 'cookies_paypal.pkl'
        url = 'https://www.paypal.com/us/home'
    else:
        raise Exception('Invalid Website')

    cookies = pickle.load(open(file_name, 'rb'))

    # Selenium requires to be on the URL you add the cookie to
    driver.get(url)

    for cookie in cookies:
        driver.add_cookie(cookie)
    
if __name__ == '__main__': 
    access_sites(product_urls)