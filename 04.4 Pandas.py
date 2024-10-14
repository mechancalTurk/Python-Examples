####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Working with Pandas #######
####### B. Ege #######


import pandas as pd


######################## LOADING DATA WITH PANDAS ##########################
csv_path = "voleyballSpieler.txt"
df = pd.read_csv(csv_path)
df.head()

##################### WORKING WITH & SAVING DATA ###########################

# Pandas has the method 'unique' to determine the unique elements in a column 
# of a data frame.
# df['<column>'].unique

df1 = pd.read_csv(csv_path)
df1.to_csv("voleyballSpieler.csv") 

############################# SERIES #######################################
# A series is a 1-dim. labeled array
data = [10,20,30,40,50]
s = pd.Series(data)
print("pd.Series(data):",s)

# Accessing Elements in Series
# Accessing by label:
print("s[2]:",s[2])
# Accessing by position:
print("s.iloc[2]:",s.iloc[2])
# Accessing multiple elements:
print("s[1:4]:",s[1:4])

# What is a DataFrames?
# A DataFrame is a 2-dim. labeled data structure with columns of potentially different data types.
# Creating DataFrames from Dictionaries:
# DataFrames can be created from dictionaries, with keys as columns and values as lists
# representing rows.
data = {'Name': ["Börtecin", "Baykal", "Gülcin", "Nuran"],"Surname":["Ege", "Yelkalan", "Ege", "Yelkalan"],
        "Birthyear":[1970, 1950, 1980, 1948],"City":["Vienna", "Istanbul", "Izmir", "Istanbul"]}
df = pd.DataFrame(data)
print("df data:\n",df)
print('type (1):', type(df))
a = df['Name']
print('type (2):',type(a))
b = df[['Name', 'Surname']]
print('type (3):',type(b))
print('\n')
print("Name, Surname:",df[['Name', 'Surname']])
print('\n')
# Finding Unique Elements:
print("unique Birthyears:",df['Birthyear'].unique)
print('\n')
# Conditional Filtering:
my_condition1 = df[df['Birthyear'] >= 1970]
print("Alle, die ab 1970 geboren:\n",my_condition1.head())
print('\n')
my_condition2 = df[(df['Birthyear'] <= 1950) & (df['City'].str.contains('Istanbul'))]
print("All, die vor dem 1951 geboren und in Istanbul wohnen:\n",my_condition2.head())
print('\n')
my_condition3 = df[(df['Birthyear'].between(1940,1980)) & (df['City'].str.contains('I'))]
print("All, die zwischen 1940 und 1980 geboren sind, in einer Stadt wohnen, deren Name mit I anfängt:\n",my_condition3.head())
print('\n')                   
# Saving the result as .csv file:
my_condition3.to_csv("my_result.csv", index=False)


################################# CONCLUSION ##############################################
# Mastering the use of Pandas Series (1-dim.) and DataFrames (2-dim.) is essential for effective data manipulation and analysis in Python.



























































