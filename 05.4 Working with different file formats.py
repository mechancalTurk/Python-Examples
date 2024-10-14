####### IBM Data Science Professional #############
####### Python for Data Science, AI & Development #
####### Working withh different file formats ######
################### B. Ege ########################

# Define different file formats such as csv, xml, and json 
# How to recognize different file types
# Write simple programs to read and output data 
# What Python libraries are needed to extract data
# How to use dataframes when collecting data

######### Reading data from CSV in Python ##########################

# Adding column name to the DataFrame

# We can add columns to an existing DataFrame using its columns attribute
# df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']

# Selecting a single column
# df['First Name']

# Selecting multiple columns
# df = df[['First Name', 'Last Name', 'Location']]

# Selecting rows using .iloc() and .loc() 
# loc() is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
# df.loc[0]
# df.loc[[0,1,2], "First Name"]
# iloc() is a indexed based selecting method which means that we have to pass integer index in the method to select specific row/column.
# df.iloc[[0,1,2],0]

# Transform Function in Pandas
#import library
import pandas as pd
import numpy as np
#creating a dataframe
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print("df:\n", df)
print("\n")
# Let’s say we want to add 10 to each element in a dataframe:
# applying the transform function
df = df.transform(func = lambda x : x + 10)
print("df:\n", df)
print("\n")
# Now we will use DataFrame.transform() function to find the square root to each element of the dataframe.
result = df.transform(func = ['sqrt'])
print("result:\n", result)
print("\n")

##############################  JSON File Format #############################

import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Serialization using dump() function¶
# json.dump() method can be used for writing to JSON file.
# Syntax: json.dump(dict, file_pointer)
# Parameters:
#   dictionary – name of the dictionary which should be converted to JSON object.
#   file pointer – pointer of the file opened in write or append mode.
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# Serialization using dumps() function
# json.dumps() that helps in converting a dictionary to a JSON object.
# It takes two parameters:
#   dictionary – name of the dictionary which should be converted to JSON object.
#   indent – defines the number of units for indentation
    
# Serializing json  
json_object = json.dumps(person, indent = 4) 
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 
# Our Python objects are now serialized to the file. For deserialize it back to 
# the Python object, we use the json.load() function:
# Opening JSON file 
with open('sample.json', 'r') as openfile: 
      # Reading from json file 
    json_object = json.load(openfile) 

print(json_object) 
print(type(json_object)) 

# Reading xml file using pandas.read_xml function
# df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 
# https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.read_xml.html

# Save Data
# dataframe.to_csv("employee.csv", index=False)

# We can also read and save other file formats, we can use similar functions 
# to pd.read_csv() and df.to_csv() for other data formats. 
# The functions are listed in the following table:
# csv:	pd.read_csv()	df.to_csv()
# json:	pd.read_json()	df.to_json()
# excel:pd.read_excel()	df.to_excel()
# hdf:	pd.read_hdf()	df.to_hdf()
# sql:	pd.read_sql()	df.to_sql()

# Data Analysis
df = pd.read_csv("diabetes.csv")

print("df.head(5):\n", df.head(5))
print("df.shape:\n", df.shape)
print("df.info():\n", df.info())
print("df.describe():\n", df.describe())
print("\n")

# Identify and handle missing values
# We use Python's built-in functions to identify these missing values. 
# There are two methods to detect missing data:
missing_data = df.isnull()
print("missing_data.head(5):\n", missing_data.head(5))
print("\n")
#missing_data = df.notnull()
#print("missing_data.head(5):\n", missing_data.head(5))
#print("\n")

# The output is a boolean value indicating whether the value that is passed into 
# the argument is in fact missing data.
# "True" stands for missing value, while "False" stands for not missing value.

# Count missing values in each column
# Using a for loop in Python, we can quickly figure out the number of missing values 
# in each column. As mentioned above, "True" represents a missing value, "False" means 
# the value is present in the dataset. In the body of the for loop the method 
# ".value_counts()" counts the number of "True" values:
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")   
# Remember, that "True" stands for missing value, while "False" stands for not missing value.
# As you can see above, there is no missing values in the dataset.    

# Correct data format
# Check all data is in the correct format (int, float, text or other).
# In Pandas, we use
#   .dtype() to check the data type
#   .astype() to change the data type
# Numerical variables should have type 'float' or 'int'.
print(df.dtypes)
# As we can see above, All columns have the correct data type.

# Visualization
# Visualization is one of the best way to get insights from the dataset. 
# Seaborn and Matplotlib are two of Python's most powerful visualization libraries.
import matplotlib.pyplot as plt
#import seaborn as sns

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
# As you can see above, 65.10% females are not Diabetic and 34.90% are Diabetic.

# SEE ALSO XLSX file format in Lab file:
# Reading data from XLSX file
# Writing and Reading with xml.etree.ElementTree










