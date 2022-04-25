from RM_Modules import *
#import mysql.connector

#mydb = mysql.connector.connect(
  #host="localhost",
  #user="yourusername",
  #password="yourpassword",
 #database="mydatabase"
#)

def right_move():
    today_1 = (date.today()).strftime("%d/%m/%Y")
    today_str = str(today_1)
    today_equation = datetime.date.today()
    yesterday = (today_equation - datetime.timedelta(days=1)).strftime("%d/%m/%Y")
    yesterday_str = str(yesterday)
    currenttime = str(datetime.datetime.now())
    Currenttime_1 = currenttime.replace(':','')

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
            house_information = agent.find("div", class_="property-information")
            house_type = agent.find("span", class_="text")
            if house_type is not None:
                lister_house_type.append(house_type.text)
            else:
                house_type = str("Not Provided")
                lister_house_type.append(house_type)
            bedrooms = house_information.find("span", {"aria-hidden" : "true"}, class_="text")
            if bedrooms == None:
                bedrooms = str('Not provided')
            if bedrooms == 'Not provided':
                lister_bedrooms.append(bedrooms)
            else:
                lister_bedrooms.append(bedrooms.text)
            added = agent.find("span", class_="propertyCard-branchSummary-addedOrReduced")
            agents = agent.find("div", class_="propertyCard-branchLogo") 
            location = agent.find("address", class_="propertyCard-address property-card-updates")
            if location is not None:
                lister_address.append(location.text)
            filter = re.sub(r'^.*?title="','',str(agents)) #Using the re.sub command to search for match='"" then replace with nothing
            filter2 = re.sub('"><img.*$', '', str(filter)) #using .replace to replace 'Logo" '> with nothing 
            added_filter = re.sub(r'^.*?Added on ','',str(added.text))
            if filter2 is not None:
                lister_agent.append(filter2)     
            lister_agent_date_added.append(added_filter)
            lister_agent_date_added_2 = [sub.replace(yesterday_count, yesterday_str) for sub in lister_agent_date_added]
            lister_agent_date_added_3 = [sub_1.replace(today_count, today_str) for sub_1 in lister_agent_date_added_2]
            lister_agent_date_added_4 = [sub_2.replace(reduced_count, '') for sub_2 in lister_agent_date_added_3]
            lister_agent_date_added_5 = [sub_3.replace(reduced_yesterday, yesterday_str) for sub_3 in lister_agent_date_added_4]

        estate_agents_pricing = doc.find_all("div", class_="propertyCard-header")
        for price in estate_agents_pricing:
            pricing = price.find("div", class_="propertyCard-priceValue")
            if pricing is not None:
                lister_price.append(pricing.text)
            else:
                lister_price.append(0)
        time.sleep(3)
        try:
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"l-container\"]/div[3]/div/div/div/div[3]/button/span"))).click()
        except:
            pass
        time.sleep(3)
        url = browser.current_url
        browser.get(url)
        doc = soup(browser.page_source, "html.parser") 
        count = count + 1

    browser.quit()

    try:
        os.mkdir(os.getcwd() + '\\output')
    except:
        pass

    def Save_to_xlsx():
        df = pd.DataFrame({'Estate agent': lister_agent, 
                            'House_location' : lister_address,
                            'House_type': lister_house_type, 
                            'Bedrooms' : lister_bedrooms, 
                            'Price' : lister_price, 
                            'Added on' : lister_agent_date_added_5})
        df.drop_duplicates(subset=None, keep="first", inplace=True) 
        Out_path = os.getcwd() + '\\output\\' + 'RightMove_' + str(Currenttime_1) + '_.xlsx'
        writer = pd.ExcelWriter(Out_path)
        df.to_excel(writer, sheet_name='test', index=False, header=True)
        writer.save()
        
    Save_to_xlsx()
    
if __name__ == "__main__":
    right_move()

