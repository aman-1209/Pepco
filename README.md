# Pepco
It is a project which logs into pepco website and takes out the information of customer bill automatically using selenium

Working of Files :

1) chromedriver.exe - It is an .exe drive of chrome which helps us to run chrome automatically using selenium
2) CustomerDetailDB.db - It is a database file which stores the data we want to extract from a website
3) Pepco.py - It is a python file which we are going to run and it will automatically do the following steps :
	a) Open the pepco website
	b) Login into the website
	c) Selects the first customer
	d) Extract the billing information of the customer and add it into database
	e) At last it will show the data in the output window
4) requirements.txt - It is a file which contains all the third party libraries required to run the script.
5) ShowDatabase_Details.py - It is an extra script to show the details added in database for future purpose.
