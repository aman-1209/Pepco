from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import pandas as pd
import sqlalchemy

# CustomerDetailDB Database
dbPath = "CustomerDetailDB.db"


# Insert Function to add Customer data into SQLite Database
def Insert(Value, dbPath):
    try:
        conn = sqlite3.connect(dbPath)
        cur = conn.cursor()

        cur.execute(
            '''insert into Details values ('%s','%s','%s','%s','%s','%s');''' % (
                Value[0], Value[1], Value[2], Value[3], Value[4], Value[5]))
        conn.commit()
        print("Details Added")
    except sqlite3.Error as error:
        msg = "Exception error : " + str(error)
        print(msg)


# Main BeautifulSoup Logic

# Chromw Web Driver
bs4 = webdriver.Chrome(executable_path=r"chromedriver.exe")
bs4.implicitly_wait(0.5)

bs4.maximize_window()
# Accessing URL
bs4.get("https://www.pepco.com/Pages/default.aspx")
time.sleep(2)

# SignIn Button Click
signIn = bs4.find_element_by_xpath('//*[@id="s4-titlerow"]/header/div/button')
signIn.send_keys(Keys.ENTER)
time.sleep(2)

# Sending username to username Field
uname = bs4.find_element_by_xpath(
    '//*[@id="main"]/div[2]/div/div/app-signin/section/form/div[1]/div/div[1]/app-input-common/label/input')
uname.send_keys('Akelius2016')
time.sleep(2)

# Sending password to password Field
upass = bs4.find_element_by_xpath(
    '//*[@id="main"]/div[2]/div/div/app-signin/section/form/div[1]/div/div[3]/app-input-masking-common/label/input')
upass.send_keys('Start1234')
time.sleep(2)

# Login Button
btncontinue = bs4.find_element_by_xpath(
    '//*[@id="main"]/div[2]/div/div/app-signin/section/form/div[2]/app-button-common[1]/button')
btncontinue.send_keys(Keys.ENTER)
time.sleep(2)

# View button to enter Customer detail page
view = bs4.find_element_by_xpath('//*[@id="changeAccountDT1"]/tbody/tr[1]/td[8]/span/span/button')
view.send_keys(Keys.ENTER)
time.sleep(2)

# Declared Array List
Details = []

# Scrapping Customer Name
CustomerName = bs4.find_element_by_xpath('/html/body/form/div[3]/div[3]/section/div/div[1]/div[1]/p[1]/span').text
print(Details.append(CustomerName))

# Scrapping Last Payment info
LastPayment = bs4.find_element_by_xpath(
    '/html/body/form/div[3]/div[3]/section/div/div[1]/div[2]/div/div[2]/div/p[1]/span').text
Details.append(LastPayment)

# Scrapping Received amount info
Received = bs4.find_element_by_xpath('/html/body/form/div[3]/div[3]/section/div/div[1]/div[2]/div/div[2]/div/p[2]/span').text
Details.append(Received)

# Scrapping Current Bill info
CurrentBill = bs4.find_element_by_xpath(
    '/html/body/form/div[3]/div[3]/section/div/div[1]/div[2]/div/div[2]/div/p[3]/span').text
Details.append(CurrentBill)

# Scrapping Due Date
DueDate = bs4.find_element_by_xpath('/html/body/form/div[3]/div[3]/section/div/div[1]/div[2]/div/div[2]/div/p[4]/span').text
Details.append(DueDate)

# Scrapping Total amount due
TotalAmountDue = bs4.find_element_by_xpath(
    '/html/body/form/div[3]/div[3]/section/div/div[1]/div[2]/div/div[2]/div/p[5]/span').text
Details.append(TotalAmountDue)

# Splitting data into (Key:Value) Pair
ValuesList = []
for D in Details:
    Value = D.split(': ')[-1]
    ValuesList.append(Value)
# Insert function declaration
Insert(ValuesList, dbPath)


# Defenintion of Creation of Database Table
def CreateTable(dbPath):
    try:
        conn = sqlite3.connect(dbPath)
        cur = conn.cursor()
        conn.execute(
            '''CREATE TABLE IF NOT EXISTS Details (Name TEXT NOT NULL, LastPayment TEXT NOT NULL, Received TEXT NOT 
                NULL, CurrentBill TEXT NOT NULL, DueDate TEXT NOT NULL, TotalAmountDue TEXT NOT NULL);''')
        conn.commit()

        # Closing database
        cur.close()
        if conn:
            conn.close()
    except sqlite3.Error as error:
        msg = "Exception error : " + str(error)
        print(msg)


CreateTable(dbPath)


# Extraction Function defenition to show data just after scrapping
def ExtractData():
    engine = sqlalchemy.create_engine('sqlite:///CustomerDetailDB.db')
    data = pd.read_sql('Select * from Details', engine)

    print(data)


ExtractData()
