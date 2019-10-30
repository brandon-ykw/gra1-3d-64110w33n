from selenium import webdriver
from joblib import Parallel, delayed
# NOTE: change to config when deploying
from config_test import product_urls
import time
import pickle

def access_sites(product_urls):
    # For concurrent bots
    Parallel(n_jobs=-1)(delayed(order)(product_url) for product_url in product_urls)

def order(product_url): 
    # Need to have chromedriver.exe in root directory
    driver = webdriver.Chrome(executable_path='./chromedriver')

    # Wait for elements to appear (in anticipation of high Grailed traffic)
    driver.implicitly_wait(300)

    cookies_grailed = pickle.load(open('cookies_grailed.pkl', 'rb'))

    # NOTE: this takes time, perhaps optimise by having subsequent lines run at specific Grailed drop time.
    insert_all_cookies(driver)
    
    # Access listing
    driver.get(product_url) 
    
    # Ensure we click PURCHASE button and not MESSAGE (happens when elements don't load fast enough)
    # NOTE: can be optimised by checking that PURCHASE has loaded
    time.sleep(1.5)

    # PURCHASE
    driver.find_element_by_xpath('//*[@id="listing-show-cta"]/div/div[1]/button[1]').click() 

    
    # CHECKOUT WITH PayPal
    driver.find_element_by_xpath('/html/body/div[14]/div/div/div/div[2]/div[2]/div[2]/button').click() 

    # NOTE: WARNING WARNING WARNING WARNING - YOU WILL PAY:
    # Pay Now (untested, might require a sleep)
    # driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/button').click()

    time.sleep(100) # testing only

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