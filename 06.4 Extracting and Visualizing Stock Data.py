####### IBM Data Science Professional #############
####### Python Project for Data Science ###########
####### Extracting and Visualizing Stock Data ##### 
################### B. Ege ########################


##### EXTRACTING && VISUALIZING STOCK DATA #####

# Extracting essential data from a dataset and displaying it is a necessary part of data science;
# therefore individuals can make correct decisions based on the data.
# In this assignment, you will extract some stock data, you will then display this data in a graph.

# Note:- If you are working in IBM Cloud Watson Studio, please replace the command for installing 
# nbformat from !pip install nbformat==4.2.0 to simply !pip install nbformat

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# ************** QUESTION-1 ****************
# Using the Ticker function enter the ticker symbol of the stock we want to extract 
# data on to create a ticker object
# The stock is Tesla and its ticker symbol is TSLA
tesla = yf.Ticker("TSLA") 

# Using the ticker object and the function history extract stock information 
# and save it in a dataframe named 'tesla_data'. 
# Set the period parameter to max so we get information for the maximum amount of time.
tesla_data = tesla.history(period="max")

# Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame 
# and display the first five rows of the tesla_data dataframe using the head function. 
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
print("\n")

# ************* QUESTION-2: ***************** 
# Use Webscraping to Extract Tesla Revenue Data
# Use the requests library to download the webpage 
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm 
# and then save the text of the response as a variable named html_data.

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

# Using BeautifulSoup or the read_html function extract the table with Tesla Revenue 
# and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.
# Tip - If you need help locating the table:
# Below is the code to isolate the table, you will now need to loop through the rows and columns like 
# in the previous lab
# soup.find_all("tbody")[1]  
# If you want to use the read_html function the table is located at index 1

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    # Finally we append the data of each row to the table
    tesla_revenue = tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)

# Execute the following line to remove the comma and dollar sign from the Revenue column.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")

# Execute the following lines to remove an null or empty strings in the Revenue column.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Display the last 5 row of the tesla_revenue dataframe using the tail function:
#print(tesla_revenue.head())
print(tesla_revenue.tail())
print("\n")

# ********* QUESTION-3: ************
# Use yfinance to Extract Stock Data
# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create 
# a ticker object. The stock is GameStop and its ticker symbol is GME.
GameStop = yf.Ticker("GME")

# Using the ticker object and the function history extract stock information and save it in a dataframe 
# named gme_data. Set the period parameter to max so we get information for the maximum amount of time.
gme_data = GameStop.history(period="max")

# Reset the index using the reset_index(inplace=True) function on the gme_data DataFrame and display 
# the first five rows of the gme_data dataframe using the head function. 
gme_data.reset_index(inplace=True)
print(gme_data.head())
print("\n")

# ********** QUESTION-4 **********
# analogous to the the Question-2!

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data, 'html.parser')
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    gme_revenue = gme_revenue.append({"Date":date, "Revenue":revenue}, ignore_index=True)
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
print(gme_revenue.tail(5))
print("\n")




