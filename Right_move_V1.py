from ast import Num
from asyncio.windows_events import NULL
from decimal import setcontext
from distutils.filelist import findall
from email import header
from lib2to3.pgen2 import driver
from operator import contains
from ssl import Options
from xml.dom.minidom import Element
from bs4 import BeautifulSoup as soup
from collections import Counter
import requests, fnmatch, re, urllib.request 
import pandas as pd
from selenium import webdriver
import datetime
from datetime import date, timedelta
import mysql.connector

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
browser = webdriver.Chrome(r'C:\Users\robru\OneDrive\Desktop\Selenium automation\Estate agent lookup\chromedriver.exe')
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
    doc = soup(browser.page_source, "html.parser") #Using b converts into html parser to be read
    estate_agents = doc.find_all("div", class_="propertyCard-content")
    estate_agents_pricing = doc.find_all("div", class_="propertyCard-header")
    for agent in estate_agents:
        try:
            house_information = agent.find("div", class_="property-information")
            house_type = house_information.find("span", class_="text")
            lister_house_type.append(house_type.text)
            bedrooms = house_information.find("span", {"aria-hidden" : "true"}, class_="text")
            added = agent.find("span", class_="propertyCard-branchSummary-addedOrReduced")
            agents = agent.find("div", class_="propertyCard-branchLogo") 
            location = agent.find("address", class_="propertyCard-address property-card-updates")
            filter = re.sub(r'^.*?title="','',str(agents)) #Using the re.sub command to search for match='"" then replace with nothing
            filter2 = re.sub('"><img.*$', '', str(filter)) #using .replace to replace 'Logo" '> with nothing 
            added_filter = re.sub(r'^.*?Added on ','',str(added.text))
        except:
            pass

        if bedrooms == None:
            bedrooms = str('Not provided')
        

        browser.implicitly_wait(1)
        if bedrooms == 'Not provided':
            lister_bedrooms.append(bedrooms)
        else:
            lister_bedrooms.append(bedrooms.text)
        if filter2 is not None:
            lister_agent.append(filter2)
     
        lister_agent_date_added.append(added_filter)
        lister_agent_date_added_2 = [sub.replace(yesterday_count, yesterday_str) for sub in lister_agent_date_added]
        lister_agent_date_added_3 = [sub_1.replace(today_count, today_str) for sub_1 in lister_agent_date_added_2]
        lister_agent_date_added_4 = [sub_2.replace(reduced_count, '') for sub_2 in lister_agent_date_added_3]
        lister_agent_date_added_5 = [sub_3.replace(reduced_yesterday, yesterday_str) for sub_3 in lister_agent_date_added_4]

        if location is not None:
            lister_address.append(location.text)

    for price in estate_agents_pricing:
        pricing = price.find("div", class_="propertyCard-priceValue")
        lister_price.append(pricing.text)

    button = browser.find_element_by_xpath('//*[@id="l-container"]/div[3]/div/div/div/div[3]/button')
    button.click()
    url = browser.current_url
    count = count + 1

print(len(lister_agent), len(lister_address), len(lister_house_type), len(lister_bedrooms), len(lister_price), len(lister_agent_date_added_5))
browser.quit()

df = pd.DataFrame({'Estate agent': lister_agent, 
                    'House_location' : lister_address,
                    'House_type': lister_house_type, 
                    'Bedrooms' : lister_bedrooms, 
                    'Price' : lister_price, 
                    'Added on' : lister_agent_date_added_5})
df.drop_duplicates(subset=None, keep="first", inplace=True) 
writer = pd.ExcelWriter('V1.xlsx')
df.to_excel(writer, sheet_name='test', index=False, header=True)
writer.save()
    

    


