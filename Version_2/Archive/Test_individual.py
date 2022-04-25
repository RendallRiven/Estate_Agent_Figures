from ast import Num
from asyncio.windows_events import NULL
from decimal import setcontext
from distutils.filelist import findall
from email import header
from lib2to3.pgen2 import driver
from operator import contains
from ssl import Options
from time import sleep, time
from xml.dom.minidom import Element
from bs4 import BeautifulSoup as soup
from collections import Counter
import requests, fnmatch, re, urllib.request 
import pandas as pd
from selenium import webdriver
import datetime
from datetime import date, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
#import mysql.connector

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="yourusername",
  #password="yourpassword",
 #database="mydatabase"
#)

today_1 = (date.today()).strftime("%d/%m/%Y")
today_str = str(today_1)
print(today_str)
today_equation = datetime.date.today()
yesterday = (today_equation - datetime.timedelta(days=1)).strftime("%d/%m/%Y")
yesterday_str = str(yesterday)

index = 0
count = 0
yesterday_count = "Added yesterday"
today_count = "Added today"
reduced_count = "Reduced on "
reduced_yesterday = 'Reduced yesterday'

lister_house_type = []
lister_bedrooms = []
lister_price = []
lister_agent = []
lister_agent_date_added = []
lister_address = []
lister_reduced = []
agent_keys = []
Count_agent = []

options = webdriver.ChromeOptions
browser = webdriver.Chrome(r'C:\Users\rober\OneDrive\Desktop\Estate_Agents\Estate_Agent_Figures\Version_2\chromedriver.exe')
url = f'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E1497&index={index}&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
browser.get(url)
urllib.request.urlretrieve(url, "rightmove.txt") # puts all html in test.txt file
doc = soup(browser.page_source, "html.parser") #Using b converts into html parser to be read
estate_agents = doc.find_all("div", class_="propertyCard-content")
estate_agents_pricing = doc.find_all("div", class_="propertyCard-header")
page_find = doc.find("div", class_="l-propertySearch-paginationWrapper")
Page_find_2 = doc.find("span", {"data-bind" : "text: total"}, class_="pagination-pageInfo").text

page = int(Page_find_2)


while count <= page:

    estate_agents = doc.find_all("div", class_="propertyCard-content")#
    for agent in estate_agents:
        added = agent.find("span", class_="propertyCard-branchSummary-addedOrReduced")
        agents = agent.find("div", class_="propertyCard-branchLogo") 
        filter = re.sub(r'^.*?title="','',str(agents)) #Using the re.sub command to search for match='"" then replace with nothing
        filter2 = re.sub('"><img.*$', '', str(filter)) #using .replace to replace 'Logo" '> with nothing 
        lister_agent.append(filter2)
        print(lister_agent)
    sleep(5)
    try:
        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"l-container\"]/div[3]/div/div/div/div[3]/button/span"))).click()
    except:
        pass
    sleep(5)
    url = browser.current_url
    browser.implicitly_wait(5)
    doc = soup(browser.page_source, "html.parser") #Using b converts into html parser to be read
    with open('Page' + str(count) + '.txt', 'w', encoding='utf-8') as f:
        f.write(doc.text)
    count = count + 1
browser.quit()

df = pd.DataFrame({'Estate agent': lister_agent, 
})
#df.drop_duplicates(subset=None, keep="first", inplace=True) 
writer = pd.ExcelWriter('V1.xlsx')
df.to_excel(writer, sheet_name='test', index=False, header=True)
writer.save()
    

    


