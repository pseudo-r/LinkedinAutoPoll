from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from datetime import datetime, date

import time, os, shutil, re, traceback, parameters, csv, os.path, time


# Functions 
def search_and_send_request():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.headless=True
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://www.linkedin.com/login')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(parameters.linkedin_username)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(parameters.linkedin_password)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]'))).click()
    time.sleep(5)
    try:
        input_2fa = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input__phone_verification_pin"]')))
        submit_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="two-step-submit-button"]')))
        while True:
            code_2fa=input("2fa code found. Please type it on the webdriver.") 
            input_2fa.send_keys(code_2fa)
            submit_button.click()
            if input_2fa:
                print('please type correct code') 
            else:
                break
    except:
        pass
    input('verify everything is working fine')
    # Open LinkedIn groups page
    driver.get('https://www.linkedin.com/groups/')


    # Find all the group links
    group_links = driver.find_elements(By.CSS_SELECTOR, 'a.link-without-visited-state')

    # Iterate over each group link
    for link in group_links:
        link.click()
        time.sleep(3)
        # Find the "Create a poll" button by aria-label
        create_poll_button = driver.find_element(By.CSS_SELECTOR, """button[aria-label='Create a poll']""")
        # Click on the button
        create_poll_button.click()
        time.sleep(3)
        # Find the input field by placeholder
        question_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="E.g., How do you commute to work?"]')
        # Enter text into the input field
        question_input.send_keys(parameters.poll_question)
        time.sleep(3)
        # Find the input field by placeholder
        option_1 = driver.find_element(By.ID, 'poll-option-1')
        # Enter text into the input field
        option_1.send_keys(parameters.option_1)
        time.sleep(3)
        # Find the input field by placeholder
        option_2 = driver.find_element(By.ID, 'poll-option-2')
        # Enter text into the input field
        option_2.send_keys(parameters.option_2)
        time.sleep(3)
        #Optional: add a new option:
        try:
            # Find the "Add option" button by text
            add_option_button = driver.find_element(By.XPATH, '//span[text()="Add option"]')
            # Click on the button
            add_option_button.click()
            time.sleep(3)
            # Find the input field by placeholder
            option_3 = driver.find_element(By.ID, 'poll-option-3')
            # Enter text into the input field
            option_3.send_keys(parameters.option_3)
            time.sleep(3)
        except:
            pass
     
        # Find the Poll duration
        duration_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="polls-duration-label"]'))

        # Select the option with value "14"
        duration_dropdown.select_by_value(parameters.poll_duration)
        time.sleep(3)
        submit_button =  driver.find_element(By.XPATH, '//span[text()="Done"]')
        submit_button.click()
        time.sleep(3)
        
if __name__ == '__main__':
    #VARIABLES
    username=parameters.linkedin_username
    password=parameters.linkedin_password
        
    # Search
    search_and_send_request()

    
     
