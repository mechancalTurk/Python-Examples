####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Working with Pandas - Practice Lab: Selecting data in a Dataframe #######
####### B. Ege #######

##########################  loc() and iloc() functions ###################################

# loc() is a label-based data selecting method which means that we have to pass the name of the row or column
# that we want to select. This method includes the last element of the range passed in it.
# Syntax: loc[row_label,column_label] --> Man darf als Index Zahlen und Labels in Kombination oder aber nur Labels angeben 

# iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method
# to select a specific row/column. This method doesn't include the last element of the range passed in it.
# Syntax: iloc[row_index,column_index]   --> Man darf als Index nur Zahlen angeben 

import pandas as pd

data = {'Student': ["David", "Samuel", "Terry", "Evan"], 'Age': ['27', '24', '22', '32'], 'Country': ['UK', 'Canada', 'China', 'USA'], 
        'Course' : ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks': ['85', '72', '89', '76']}
df = pd.DataFrame(data)
print('df:',df)

# Access the value on the first row and first column in the dataframe
print('df.iloc[0,0]:', df.iloc[0,0])
print('df.iloc[0,2]:', df.iloc[0,2])
print('df.loc[0,Course]:', df.loc[0,'Course'])

df2 = df
df2 = df2.set_index("Course")
print('df2 (index=Course):',df2.head())

df3 = df
df3 = df3.set_index("Age")
print('df3 (index=Age):',df3.head())

#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#display the result df
print("df:\n",df)
print('\n')
x= df[['ID']]
print('x:\n',x)
print('\n')

z = df[['Department','Salary','ID']]
print('z:\n',z)
print('\n')

# Access the value on the first row and first column in the dataframe
print('df.iloc[0,0]:', df.iloc[0,0])
print('df.iloc[0,2]:', df.iloc[0,2])
print('df.loc[0,Salary]:', df.loc[0,'Salary'])
print('\n')

df4 = df
df4 = df4.set_index("Name")
print('df4.set_index("Name"):\n', df4.head())
print('\n')

# Now, let us access the column using the name
print("df4.loc['Jane','Salary']:",df4.loc['Jane','Salary'])
print("df4.loc['Jane','Department']:",df4.loc['Jane','Department'])
# Now, Use the iloc() function to get the Salary of Mary
print("df4.iloc[3,0]:",df4.iloc[3,0])
print("df4.iloc[3,1]:",df4.iloc[3,1])
print("df4.iloc[3,2]:",df4.iloc[3,2])
print("\n")
#df5 = df
#df5 = df5.set_index("ID")
#print('df5.set_index("ID"):\n', df5.head())
#print('\n')
#print("df5.iloc[3,0]:",df5.iloc[3,0])
#print("df5.iloc[3,1]:",df5.iloc[3,1])
#print("df5.iloc[3,2]:",df5.iloc[3,2])
#print('\n')

# Conditional Filtering:
my_condition4 = df[df['Salary'] >= 70000]
print("Alle, die mehr als 70000 verdienen:",my_condition4.head())
print("\n")

############################# Slicing ###############################

# Slicing uses the [] operator to select a set of rows and/or columns from a DataFrame
# To slice out a set of rows, you use this snytax: data[start:stop]
# NOTE: When slicing in pandas, the start bound is included in the output

# loc() is a label-based data selecting method which means that we have to pass the name of the row or column
# that we want to select. This method includes the last element of the range passed in it.
# Syntax: loc[row_label,column_label] --> Man darf als Index Zahlen und Labels in Kombination oder aber nur Labels angeben 

# iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method
# to select a specific row/column. This method doesn't include the last element of the range passed in it.
# Syntax: iloc[row_index,column_index]  --> Man darf als Index nur Zahlen angeben 

print("***********  SCLICING *************")
print("df.iloc[0:2]:\n", df.iloc[0:2])
print("\n")
print("df.iloc[0:2, 0:3]:\n", df.iloc[0:2, 0:3])
print("\n")
print("df.loc[0:2,'ID':'Department']:\n", df.loc[0:2,'ID':'Department'])
print("\n")

print("Achtung! The index is 'Name':\n", df4.head())
print("\n")
print("df4.loc['Rose':'Jane', 'ID':'Department']:\n", df4.loc['Rose':'Jane', 'ID':'Department'])  
print("\n")

# Now, set the index from 'Name' to 'ID'
df4 = df
df4 = df4.set_index("ID")
print('Now, the index is set from Name to ID df4.set_index("ID"):\n', df4.head())
print('\n')
print("df4.loc[1:3, 'Name':'Department']: (Index=ID!)\n", df4.loc[1:3, 'Name':'Department'])  
print('\n')


####### Siehe dafür im IBM-Cloud: Working with Pandas - Hands on Lab - Loading Data with Pandas ###########
###########################   Quiz on DataFrame      ############################
# Auskommentiert, weil es sich hier um eine andere Datenmenge handelt, sonst alles richtig!

# Read data from Excel File and print the first five rows

# xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
# await download(xlsx_path, "TopSellingAlbums.xlsx")
# df = pd.read_excel("TopSellingAlbums.xlsx")
# df.head()

# Use a variable q to store the column Rating as a dataframe:
# q = df[['Rating']]

# Assign the variable q to the dataframe that is made up of the column Released and Artist:
# q = df[['Released','Artist']]

# Access the 2nd row and the 3rd column of df:
# df.iloc[1,2]

# Use the following list to convert the dataframe index df to characters and assign it to df_new; 
# find the element corresponding to the row index a and column 'Artist'. 
# Then select the rows a through d for the column 'Artist':
# new_index=['a','b','c','d','e','f','g','h']
# df_new = df
# den neuen Index a bis h festlegen anstatt 0 bis 7 wie es ursprünglich war
# df_new.index = new_index
# find the element corresponding to the row index a and column 'Artist':
# df_new.iloc[0,0]  == df_new.loc['a','Artist'] --> Michael Jackson
# then select the rows a through d for the column 'Artist':
# df_new.loc['a':'d','Artist']


################  PRACTICE QUIZ  ################
# Q: What python object do you cast to a dataframe?
# dictionary

# Q: How would you access the first-row and first column in the dataframe df?
# df.ix[0,0]

# Q: What is the proper way to load a CSV file using pandas?
# pandas.read_cvs('data.csv')












