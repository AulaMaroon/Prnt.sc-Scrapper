from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import base64
import imghdr
import random
import string
import time
from tqdm import tqdm

chromeDriverPath='.\chromedriver.exe'
driver=webdriver.Chrome(chromeDriverPath)
driver.set_window_position(-20000,0)

def loaderandgrabber():
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(6))
    url = "https://prnt.sc/" + result_str
    driver.get(url)
    os.system('cls')
    spliturl = url.rsplit('/', 1)[-1]
    return spliturl

def downloader_image(download_path, file_name):
    fname = download_path + file_name + ".png"
    elenemt = driver.find_element(By.CLASS_NAME, "screenshot-image")
    elenemt.screenshot(fname)

    
def starter():
    time.sleep(5)
    os.system('cls')
    amount = input("Enter The Ammount Of Picture To Get : ")
    amount = int(amount)
    totaldownloaded = 1
    pbar = tqdm(total=amount)
    while totaldownloaded <= amount:
        spliturl = loaderandgrabber()
        downloader_image("images/", spliturl)
        totaldownloaded += 1
        print("Downloading Images")
        print()
        pbar.update(n=1)
    driver.close()

starter()