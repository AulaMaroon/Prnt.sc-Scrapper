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
    while True:
        letters = string.ascii_lowercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(6))
        try:
            if os.path.isfile('images/' + result_str + '.png'):
                raise Exception("File Exist")
        except:
            continue
        else:
            break
    print('2')
    url = "https://prnt.sc/" + result_str
    driver.get(url)
    os.system('cls')
    try:
        ss = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/img')
        img_url = ss.get_attribute('src')
        base64Img = img_url.replace("data:image/png;base64,", "")
        spliturl = url.rsplit('/', 1)[-1]
    except:
        pass
    return base64Img, spliturl

def downloader_image(download_path, url, file_name):
    try:
        sample = base64.b64decode(url)
        for tf in imghdr.tests:
            res = tf(sample, None)
            if res:
                break
        if res == None:
            fname = download_path + file_name + ".png"
            elenemt = driver.find_element(By.CLASS_NAME, "screenshot-image")
            elenemt.screenshot(fname)
        else:
            imgdata = base64.b64decode(url) 
            path = download_path + file_name + "." + res
            with open(path, 'wb') as f:
                f.write(imgdata)
    except:
        pass
    
def starter():
    time.sleep(5)
    os.system('cls')
    amount = input("Enter The Ammount Of Picture To Get : ")
    amount = int(amount)
    totaldownloaded = 1
    pbar = tqdm(total=amount)
    while totaldownloaded <= amount:
        try:
            url, spliturl = loaderandgrabber()
            downloader_image("images/", url, spliturl)
        except:
            pass
        totaldownloaded += 1
        print("Downloading Images")
        print()
        pbar.update(n=1)
    driver.close()

starter()