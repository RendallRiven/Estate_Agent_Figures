from io import BytesIO
from itertools import count
from turtle import right, width
from bs4 import BeautifulSoup as soup
from collections import Counter
import requests, fnmatch, re, urllib.request 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from PIL import Image
import os

print('Welcome to Chrome instragram web scrapper. Please ensure this profile does not break any infringe on privacy on users or instragram rules. The developers take no responsibilty of how this program is used.')

insta_posts = input('Please enter the number of posts on the page: ')
path = input ('Please input the save path: ')
insta_url = input('Please input the Instagram profile you want to scrap: ')
raw_key = input('Close the Chrome browser and press any key to continue...')
img_num = int(insta_posts)
county = 0
user_profile = os.environ['USERPROFILE']
op = Options()
op.add_argument(f"user-data-dir={user_profile}\\AppData\\Local\\Google\\Chrome\\User Data")
op.add_argument("profile-directory=Default")
op.add_argument("--disable-extensions")
#op.add_experimental_option("detach", True)
ser = Service("chromedriver.exe")

browser = webdriver.Chrome(service=ser, options=op)
browser.maximize_window()
browser.implicitly_wait(5)
browser.get(insta_url)

try:
    Allow_cookies = browser.find_element_by_link_text("Allow essential and optional cookies")
    Allow_cookies.click()
    time.sleep(0.5)
except:
    pass

time.sleep(0.5)

picture = (browser.find_element_by_css_selector("._9AhH0"))

time.sleep(0.5)
picture.click()
with open ('insta.txt', 'w', encoding='utf-8') as f:
    f.write(browser.page_source)

time.sleep(0.3)

while county < int(img_num):
    time.sleep(0.99)
    screenshot = browser.save_screenshot("picture-%s.png" % county)
    time.sleep(0.5)
    im = Image.open("picture-%s.png" % county)

    width, height = im.size
    left = 240
    top = 32
    right = 1055
    bottom = 755

    im = im.crop((left, top, right, bottom))
    filename = '\\New%s.png' % county
    im.save(path + filename)
    im.show
    os.remove("picture-%s.png" % county)
    next = browser.find_element_by_css_selector(".l8mY4 .\_8-yf5")
    next.click()

    county = county + 1

browser.quit()
