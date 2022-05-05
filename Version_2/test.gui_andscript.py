from RM_Modules import *


from ctypes.wintypes import SIZE
from functools import partial
import tkinter as tk
from tkinter import BOTH, INSERT, Button, Frame, Canvas, Menu, StringVar, Variable
from tkinter import font
from tkinter.filedialog import askopenfile
from turtle import bgcolor, pd, right
from PIL import Image, ImageTk
from numpy import insert, pad, size
import pandas as pd
from pyparsing import col
from V2_InProgress import *
from tkinter import messagebox
import customtkinter
import SQL_query_reporting

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def quit_app():
    root.destroy()

def main_gui_run():
    global root
    root=customtkinter.CTk()
    root.title('Data Collection')
    root.iconbitmap(os.getcwd() + "\\Analyte.ico")
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    w = 800 # width for the Tk root
    h = 350 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    menubar = Menu(root, background='#ff8000', foreground='black', activebackground='black', activeforeground='black')  
    file = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')  
    file.add_command(label="Exit", command= quit_app)  
    file.add_separator
    menubar.add_cascade(label="File", menu=file)

    settings = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    settings.add_command(label="URL settings", command="")
    menubar.add_cascade(label="Settings", menu=settings)

    help = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    help.add_command(label="About", command=help_about)
    menubar.add_cascade(label="Help", menu=help)

    canvas = customtkinter.CTkCanvas(root, width=600, height=30)
    canvas.grid(columnspan=3)

    head = customtkinter.CTkFrame(root, width=800, height=220)
    head.grid(columnspan=3, rowspan=4, row=0)

    body = customtkinter.CTkFrame(root, width=800, height=199)
    body.grid(columnspan=3, rowspan=4, row=2)
    
    text_var = tk.StringVar(value="CTkLabel")

    label = tk.Label(root, font=('Arial', 25), text="Housing Analytics tool", bg='#292929', fg='Red')
    label.grid(column=0,columnspan=3, row=1)

    User_input_url = customtkinter.CTkLabel(root,text='URL')
    User_input_url.grid(column=0, row =2, pady=10)

    global url_entry
    url_entry = StringVar()
    User_input_url = customtkinter.CTkEntry(root, textvariable=url_entry)
    User_input_url.grid(column=1, row=2)

    send_url = partial(right_move, url_entry)

    postcode = customtkinter.CTkLabel(root,text='Postcode')
    postcode.grid(column=0, row =3, pady=10)

    postcode_input = customtkinter.CTkEntry(root)
    postcode_input.grid(column=1, row = 3)

    right_move_but = customtkinter.CTkButton(root, command=send_url, text="Rightmove")
    right_move_but.grid(row=2, column=2)
    Disabled = customtkinter.CTkButton(root, text="DISABLED") 
    Disabled.grid(row=3, column=2)

    Download_all = customtkinter.CTkButton(root, text='Download all time data', command=SQL_query_reporting.DB_download)
    Download_all.grid(column=1, row= 4)

    root.config(menu=menubar)
    root.mainloop()

def help_about(): 
    global rooty    
    rooty=customtkinter.CTk()
    rooty.title('About')
    rooty.iconbitmap(os.getcwd() + "\\Analyte.ico")
    ws = rooty.winfo_screenwidth() # width of the screen
    hs = rooty.winfo_screenheight() # height of the screen
    w = 215 # width for the Tk root
    h = 80 # height for the Tk root
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    rooty.geometry('%dx%d+%d+%d' % (w, h, x, y)) #Geometer is used to set where the application will open on the screen


    text = customtkinter.CTkLabel(rooty, text="Analyte.uk \n Estate agents data analytics tool. \n Version 1.01 \n All rights reserved")  
    text.grid(column=1, row=1)

    rooty.wm_protocol("WM_DELETE_WINDOW", destory_window)
    rooty.mainloop()
    
def destory_window():
    rooty.destroy()


main_gui_run()


def right_move(url_entry):
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
    import main_gui
    URL_initial = url_entry.get()
    print(URL_initial)
    url = URL_initial
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
    
    def save_to_SQL():
        conn = sqlite3.connect("C:\SQLite\EST_database.db")       
        df = pd.DataFrame({'Estate_agent': lister_agent, 
                            'House_location' : lister_address,
                            'House_type': lister_house_type, 
                            'Bedrooms' : lister_bedrooms, 
                            'Price' : lister_price, 
                            'Added_on' : lister_agent_date_added_5})
        df.drop_duplicates(subset=None, keep="first", inplace=True) 
        df.to_sql("House_data", conn,if_exists="replace", index=False)
         
    
    save_to_SQL()
    
if __name__ == "__main__":
    right_move(url_entry)
