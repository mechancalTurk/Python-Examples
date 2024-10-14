####### IBM Data Science Professional #############
####### Python Project for Data Science ###########
####### Extracting Stock Data Using a Web Scraping 
################### B. Ege ########################

# Not all stock data is available via the API in this assignment; (therefore)
# you will use web-scraping to obtain financial data.
# You will extract and share historical data from a web page using the
# BeatifulSoup library.

# !mamba install bs4==4.10.0 -y
# !mamba install html5lib==1.1 -y 
# !pip install lxml==4.6.4
# already installed via cmd shell.

#python --version

import pandas as pd
import requests
from bs4 import BeautifulSoup

# In Python you can ignore warnings using the warnings module
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Now, we will extract Netflix stock data:
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# On the following web page we have a table with columns name (Date, Open, High, Low, close, adj close volume) 
# out of which we must extract following columns: Date, Open, High, Low, Close, Volume

# STEPS for extracting the data:

# STEP-1: Send a HTTP request to the web page 

# The requests.get() method takes a URL as its first argument, which specifies the location of the resource 
# to be retrieved. In this case, the value of the url variable is passed as the argument to the requests.get() 
# method, because you will store a web page URL in a url variable.

# Use the .text method for extracting the HTML content as a string in order to make it readable
data = requests.get(url).text
print(data)


# STEP-2: Parse the HTML content

# Create a new BeautifulSoup object in Python, you need to pass two arguments to its constructor:
# 1. The HTML or XML content that you want to parse as a string.
# 2. The name of the parser that you want to use to parse the HTML or XML content. 
# This argument is optional, and if you don't specify a parser, BeautifulSoup will use the default HTML parser 
# included with the library. here in this lab we are using "html5lib" parser.

soup = BeautifulSoup(data, 'html5lib')

print("\n")
title = soup.find("title")
print("title of the table: \n", title)
print("\n")

# STEP-3: Identify the HTML tags
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Working on HTML table
# These are the following tags which are used while creating HTML tables.
# <table>: This tag is a root tag used to define the start and end of the table. All the content of the table is enclosed within these tags.
# <tr>: This tag is used to define a table row. Each row of the table is defined within this tag.
# <td>: This tag is used to define a table cell. Each cell of the table is defined within this tag. You can specify the content of the cell between the opening and closing tags.
# <th>: This tag is used to define a header cell in the table. The header cell is used to describe the contents of a column or row. By default, the text inside a tag is bold and centered.
# <tbody>: This is the main content of the table, which is defined using the tag. It contains one or more rows of elements.


# STEP-4: 
# A - Extracting data using BeatifulSoup method (Netflix)
# We will use find() and find_all() methods of the BeautifulSoup object to locate the table body and table row respectively in the HTML.
# The find() method will return particular tag content.
# The find_all() method returns a list of all matching tags in the HTML.

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
print("\n")
print("****** A - Extracting data using BeatifulSoup method (Netflix) ******\n")
print(netflix_data.head())
print("\n")

# B - Extracting data using pandas library 
# We can also use the pandas read_html function from the pandas library and use the URL for extracting data
read_html_pandas_data = pd.read_html(url)
# OR you can convert the BeatifulSoup object to a String
read_html_pandas_data = pd.read_html(str(soup))
# Because there is only one table on the page, just take the first table in the returned list:
netflix_dataframe = read_html_pandas_data[0]
print("****** B - Extracting data using pandas library (Netflix) ******\n")
print(netflix_dataframe.head())
print("\n")

############# EXERCISE: Use Webscraping to Extract Stock Data  (AMAZON) ##################

# Use the requests library to download the webpage 
# Save the text of the response as a variable named html_data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
data2 = requests.get(url).text 
# Parse the html data using beautiful_soup:
soup = BeautifulSoup(data2, 'html5lib')

# What is the content of the title attribute?
title = soup.find("title")
print("title of the table: \n", title)
print("\n")

# Using BeautifulSoup, extract the table with historical share prices and store it into a data frame 
# named amazon_data. The data frame should have columns Date, Open, High, Low, Close, Adj Close, and Volume. 
# Fill in each variable with the correct data from the list col.

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    # Finally we append the data of each row to the table
    amazon_data = amazon_data.append({"Date":date, "Open":open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    
    print("amazon_data.append: \n", date, open) 
print("\n")
print("****** Extracting data using pandas library (Amazon) ******\n")
print(amazon_data.head())
print("number of rows:", len(amazon_data.index))
print("\n")

#  What are the names of the columns in the data frame?
print("What are the names of the columns in the data frame?")
print(amazon_data.columns[0])
print(amazon_data.columns[1])
print(amazon_data.columns[2])
print(amazon_data.columns[3])
print(amazon_data.columns[4])
print(amazon_data.columns[5])
print(amazon_data.columns[6])
print("\n")



# What is the Open of the last row of the amazon_data data frame?
last_row = len(amazon_data.index)
open_value = amazon_data.iloc[last_row-1, 1]
print("What is the Open of the last row of the amazon_data data frame: ", open_value)
print("\n")




