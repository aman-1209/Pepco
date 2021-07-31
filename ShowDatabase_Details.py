from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3
import pandas as pd
import sqlalchemy

# Extraction Function defenition to show data just after scrapping
def ExtractData():
    engine = sqlalchemy.create_engine('sqlite:///CustomerDetailDB.db')
    data = pd.read_sql('Select * from Details', engine)

    print(data)


ExtractData()