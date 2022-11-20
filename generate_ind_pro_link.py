#
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

#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

#
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

# chrome_options=opts
#driver = webdriver.Chrome()
if __name__ == "__main__":
    import undetected_chromedriver.v2 as uc

    driver = uc.Chrome()
    linksFileNumber = 2
    links = pd.read_csv(f"links{linksFileNumber}.txt", header=None)
    #linksFile = open(f"links{linksFileNumber}.txt", 'r')

    urls = links[0]


    driver.delete_all_cookies()  # Deletes all the cookies

    base_page_url = "https://www.whitepages.com/"
    driver.get(base_page_url)
    pageSource = driver.page_source
    f = open(f"profile-links{linksFileNumber}_1.txt", "a")
    failed_links_file = open(f"failed-links{linksFileNumber}_1.txt", "a")
    i = 0
    #urls = urls[300000:]
    #for index,url in enumerate(urls):
    #linksFile.
    for index,url in enumerate(urls):
        time.sleep(2)
        # if i >= 5:
        #     i=0
        #     driver.close()
        #     driver = webdriver.Chrome()
        driver.delete_all_cookies()  # Deletes all the cookie
        driver.get(url)
        i += 1
        try:
            checkBox = driver.find_element(By.ID, "tos-checkbox")
            if checkBox:
                checkBox.click()
                btnContToResults = driver.find_element(
                    By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/button"
                )
                if btnContToResults:
                    btnContToResults.send_keys(Keys.RETURN)
        except Exception as e:
            print(e)
            #failed_links_file.write(f"{index},{url}\n")

        try:
            profile_links = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[2]/a")
            for p in profile_links:
                plink = p.get_attribute("href")
                #print("here")
                print(f"{index},{plink}")
                f.write(f"{index},{plink}\n")
            # break
        except Exception as e:
            print(e)
            failed_links_file.write(f"{index},{url}\n")
        f.flush()
    f.close()
    failed_links_file.close()  #

    # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path

    # chrome_options=opts
    # driver = webdriver.Chrome()
