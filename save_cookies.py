from selenium import webdriver
import pickle
import time

def save_grailed_cookies():
    driver = webdriver.Chrome()
    driver.get('https://www.grailed.com')

    # Pause to login (antipate Captchas)
    time.sleep(100) 

    cookies = driver.get_cookies()

    delete_expiry(cookies)
    
    pickle.dump(cookies , open("cookies_grailed.pkl","wb"))

def save_paypal_cookies(): 
    driver = webdriver.Chrome()
    driver.get('https://www.paypal.com')

    # Pause to Login
    time.sleep(30) 

    cookies = driver.get_cookies()

    delete_expiry(cookies)
    
    pickle.dump(cookies , open("cookies_paypal.pkl","wb"))

def print_pickle():
    pickle_in_grailed = open('cookies_grailed.pkl', 'rb')
    pickle_load_grailed = pickle.load(pickle_in_grailed)
    print(pickle_load_grailed)

    pickle_in_paypal = open('cookies_paypal.pkl', 'rb')
    pickle_load_paypal = pickle.load(pickle_in_paypal)
    print(pickle_load_paypal)

def delete_expiry(cookies): 
    for cookie in cookies:
        # Bug introduced in latest Chrome
        if 'expiry' in cookie:
            del cookie['expiry']

if __name__ == '__main__': 
    save_grailed_cookies()
    save_paypal_cookies()
    # print_pickle()