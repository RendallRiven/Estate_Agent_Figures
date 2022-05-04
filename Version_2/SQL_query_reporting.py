import sqlite3
from turtle import pd
import pandas
import os
import datetime

def DB_download():

    currenttime = str(datetime.datetime.now())
    Currenttime_1 = currenttime.replace(':','')

    conn = sqlite3.connect("C:\SQLite\EST_database.db")  
    script = """select * from House_data"""

    df = pandas.read_sql_query(script, conn)

    try:
        os.mkdir(os.getcwd() + '\\data')
    except:
        pass

    writer = pandas.ExcelWriter(os.getcwd() + '\\data\\' +'SQL' + str(Currenttime_1) + '.xlsx')
    df.to_excel(writer)
    writer.save()

    path = os.getcwd() + '\\data'
    path = os.path.realpath(path)
    os.startfile(path)

if __name__ == '__main__':
    DB_download()