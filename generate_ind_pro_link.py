# %%
import html5lib
from matplotlib.pyplot import axes, axis
import requests
from bs4 import BeautifulSoup
import os
import string
import html
import time
import pandas as pd
import re
import json
import time
# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

# %%
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

#chrome_options=opts
driver = webdriver.Chrome()

links = pd.read_csv("D:\midTT\links.txt", header=None)
urls = links[0]


driver.delete_all_cookies() # Deletes all the cookies

base_page_url = 'https://www.whitepages.com/'
driver.get(base_page_url)
pageSource = driver.page_source
f = open("profile-links.txt", "w")
failed_links_file = open("failed-links.txt", "w")
for url in urls:
    time.sleep(2)
    driver.delete_all_cookies() # Deletes all the cookie
    driver.get(url)
    try:
        checkBox = driver.find_element(By.ID,'tos-checkbox')
        if checkBox:
            checkBox.click()
            btnContToResults = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[2]/button')
            if btnContToResults:
                btnContToResults.send_keys(Keys.RETURN)
    except Exception as e:
        print(e)
    try:
        profile_links = driver.find_elements(By.XPATH,'/html/body/div[3]/div/div[2]/a')
        for p in profile_links:
            plink = p.get_attribute('href')
            print(plink)
            f.write(f'{plink}\n')    
        #break
    except Exception as e:
        print(e)
        failed_links_file.write(url+'\n')
f.close()
failed_links_file.close()