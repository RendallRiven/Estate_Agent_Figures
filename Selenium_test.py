from ast import Num
from asyncio import gather
from asyncio.windows_events import NULL
from decimal import setcontext
from distutils.filelist import findall
from email import header
from lib2to3.pgen2 import driver
from operator import contains
from ssl import Options
from time import time
from xml.dom.minidom import Element
from bs4 import BeautifulSoup as soup
from collections import Counter
import requests, fnmatch, re, urllib.request 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import date, timedelta
import mysql.connector

C_options = Options()
C_options.add_argument("user-data-dir=C:\\Users\\robru\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
browser = webdriver.Chrome(executable_path=r'C:\Users\robru\OneDrive\Desktop\Selenium automation\Estate agent lookup\chromedriver.exe', options=C_options)

google_search = input('Please enter what you would like to search in Google ')

url = f'https://www.google.com/'
browser.get(url)

#urllib.request.urlretrieve(url, "rightmove.txt") # puts all html in test.txt file
doc = soup(browser.page_source, "html.parser") #Using b converts into html parser to be read
test = browser.find_element_by_name("q")
test = browser.find_element_by_xpath('//*[@id="input"]')
test.send_keys(google_search)
button = browser.find_element_by_xpath('//*[@id="icon"]')
button.click()
url = browser.current_url
print(url)

doc = soup(browser.page_source, "html.parser")
urllib.request.urlretrieve(url, "Google HTML return.txt")

gather_urls = doc.find_all("div", class_="jtfYYd")

#for i in gather_urls:





#H3LC20lb MBeuO DKV0Md
time(5)
browser.quit()

    

    


