import time
import pandas as pd
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller

print('installing chrome driver')
chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

# chrome_options=opts
if __name__ == "__main__":
    print('importing undetected_chromedriver')
    import undetected_chromedriver as uc
    print('creating driver')
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument('--window-size=1920,1080')
    #options.add_argument("--headless")
    driver = uc.Chrome(use_subprocess=True, options=options)
    print('reading csv')
    links = pd.read_csv("profile-links.txt", header=None)
    print('taking ony urls')
    urls = links[1]
    print(f'urls length original is {len(urls)}')
    driver.delete_all_cookies()  # Deletes all the cookies
    for i in [41,37,42,47,1368,2521,702,16]:
        urls = urls[i:]
        print(f'urls length after moving {i} is {len(urls)}')
    # base_page_url = 'https://www.whitepages.com/'
    # driver.get(base_page_url)
    print('openig files')
    f = open("profile-data.json", "a")
    failed_file = open("profile-data-failed.json", "a")
    index = -1
    for url in urls:
        try:
            index += 1
            print(f'fetchig index {index}')
            print('deleting cookies')
            driver.delete_all_cookies()  # Deletes all the cookie
            print(f'opening url = {url}')
            driver.get(url)
            print('sleeping...')
            time.sleep(10)
            print('extractig data')
            path = "/html/body/script[1]"
            script = driver.find_element(By.XPATH, path)
            name1 = script.get_attribute("innerHTML")
            startIndex = name1.index('{amplitudeEvent:"')

            end = name1.index('url:"https:\\u002F\\u002Fwww.whitepages.com', startIndex)
            endIndex = name1.index("]", end)
            jsonMy = name1[startIndex:endIndex]
            # print(json)
            jsonMy = re.sub("((?=\D)\w+):", r'"\1":', jsonMy)
            jsonMy = re.sub(": ((?=\D)\w+)", r':"\1"', jsonMy)
            # print(jsonMy)
            from string import ascii_lowercase, ascii_uppercase

            jsonMy = jsonMy.replace('","', '", "')
            for c in ascii_lowercase:
                jsonMy = jsonMy.replace(f":{c},", f':"{c}",')
                jsonMy = jsonMy.replace('":' + c + "}", '":"' + c + '"}')
                for d in ascii_lowercase:
                    jsonMy = jsonMy.replace(f":{c}{d},", f':"{c}{d}",')
                    jsonMy = jsonMy.replace('":' + c + d + "}", '":"' + c + d + '"}')
                for d in ascii_uppercase:
                    jsonMy = jsonMy.replace(f":{c}{d},", f':"{c}{d}",')
                    jsonMy = jsonMy.replace('":' + c + d + "}", '":"' + c + d + '"}')
            for c in ascii_uppercase:
                jsonMy = jsonMy.replace(f":{c},", f':"{c}",')
                jsonMy = jsonMy.replace('":' + c + "}", '":"' + c + '"}')
                for d in ascii_uppercase:
                    jsonMy = jsonMy.replace(f":{c}{d},", f':"{c}{d}",')
                    jsonMy = jsonMy.replace('":' + c + d + "}", '":"' + c + d + '"}')
                for d in ascii_lowercase:
                    jsonMy = jsonMy.replace(f":{c}{d},", f':"{c}{d}",')
                    jsonMy = jsonMy.replace('":' + c + d + "}", '":"' + c + d + '"}')
            jsonMy = jsonMy.replace('"url":""https"', '"url":"https').replace(
                '":_,"', '":"_","'
            )
            jsonMy = jsonMy.replace('":$', '":"$"')
            print("writing to file")
            f.write(jsonMy + ",\n")
            f.flush()
        except Exception as e:
            print(e)
            failed_file.write(url+'\n')
            failed_file.flush()
    f.close()
    failed_file.close()

