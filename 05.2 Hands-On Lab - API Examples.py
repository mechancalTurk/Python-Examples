####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #
####### Hands-on Lab - API Examples #######
################### B. Ege ########################


# Objectives
# After completing this lab you will be able to:
#   Load and use RandomUser API, using RandomUser() Python library
#   Load and use Fruityvice API, using requests Python library
#   Load and use Open-Joke-API, using requests Python library

# The purpose of this notebook is to provide more examples on how to use simple APIs. 
# As you have already learned from previous videos and notebooks, 
# API stands for Application Programming Interface and is a software intermediary 
# that allows two applications to talk to each other.

# The advantages of using APIs:
#   Automation: Less human effort is required and workflows can be easily updated to become faster and more productive
#   Efficiency: It allows to use the capabilities of one of the already developed APIs than to try to 
#               in dependently implement some functionality from scratch
# The disadvantage of using APIs:
#   Security: If the API is poorly integrated, it means it will be vulnerable to attacks!


# Example 1: RandomUser API
# Bellow are Get Methods parameters that we can generate. For more information on the parameters, please visit this documentation page
# https://randomuser.me/documentation

# To start using the API you can install the randomuser library running the pip install command.
# pip install randomuser

# Then, we will load the necessary libraries
from randomuser import RandomUser
import pandas as pd

#################  EXAMPLE-1 #######################################
print("\n")
print("******************* Example-1 *******************:\n")
# First, we wil create a random user object:
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users:
some_list = r.generate_users(10)
print("r.generate_users(10):", some_list)

# The "Get Methods" functions mentioned at the beginning of this notebook, 
# can generate the required parameters to construct a dataset. 
# For example, to get full name, we call get_full_name() function:
name = r.get_full_name()
# print("r.get_full_name:", name)

# Let's say we only need 10 users with full names and their email addresses. 
# We can write a "for-loop" to print these 10 users.
for user in some_list:
    print("Full name:", user.get_full_name(), " ", "Email:",user.get_email())

# generate photos of the random 10 users:
for user in some_list:
    print("Picture:", user.get_picture())

# To generate a table with information about the users, we can write a function containing 
# all desirable parameters. For example, name, gender, city, etc. 
# The parameters will depend on the requirements of the test to be performed. 
# We call the Get Methods, listed at the beginning of this notebook. 
# Then, we return pandas dataframe with the users.
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()
df1 = pd.DataFrame(get_users())
# Now we have a pandas dataframe that can be used for any testing purposes that the tester might have.
print(df1.head())
print("\n")
print("******************* Example-2 *******************:\n")
# Another, more common way to use APIs, is through requests library! 
# The next lab, Requests and HTTP, will contain more information about requests.
# We will start by importing all required libraries.

import requests
import json

# We will obtain the fruityvice API data using requests.get("url")
# The data is in a json format
data = requests.get("https://fruityvice.com/api/fruit/all")
# We will retrieve results using json.loads() function:
results = json.loads(data.text)
# We will convert our json data into pandas data frame.
pd.DataFrame(results)
# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, 
# so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
print(df2)
# Let's see if we can extract some information from this dataframe. 
# Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
print("cherry:", cherry)
print("family:", cherry.iloc[0]['family']," ", "genus:", cherry.iloc[0]['genus'])

# Now, find out how many calories are contained in a banana:
banana = df2.loc[df2["name"] == "Banana"]
print("Banana:", banana)
print("family:", banana.iloc[0]['nutritions.calories'])

print("\n")
print("******************* Example-3 *******************:\n")

# Big List of Free and Open Public APIs: 
# https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

# Official Joke API
# This API returns random jokes from a database. The following URL can be used to retrieve 10 random jokes.
# https://official-joke-api.appspot.com/jokes/ten

# Using requests.get("url") function, load the data from the URL.
data2 = requests.get("https://official-joke-api.appspot.com/jokes/ten")

# Retrieve results using json.loads() function.
results2 = json.loads(data2.text)

# Convert json data into pandas data frame and drop the type and id columns.
df3 = pd.DataFrame(results2)
print(results2)
N = len(results2)
# print("the length of results2 set:", N)

for i in range(0,N):
    print("type:", df3.iloc[i, 0], " ", "id:", df3.iloc[i, 3])

for i in range(0,N):
    print("type:", df3.loc[i, "type"], " ", "id:", df3.loc[i, "id"])

#df3.drop(columns=["type","id"],inplace=True)
#print("df3:", df3)




