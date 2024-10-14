####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### REST APIs & HTTP Requests #######
####### B. Ege ########################

# In this video, we will discuss the HTTP protocol using the Requests Library 
# a popular method for dealing with the HTTP protocol in Python In this video, 
# we will review Python library requests for Working with the HTTP protocols. 
# We will provide an overview of Get Requests and Post Requests Let’s review 
# the Request Module in Python. This is one of several libraries including: 
# httplib, urllib, that can work with the HTTP protocol. 
# Requests is a python Library that allows you to send HTTP/1.1 requests easily.

#######################   REQUEST MODULE IN PYTHON ######################

print("\n")
print("################## REQUEST MODULE IN PYTHON ##########################\n")

import requests
# Requests is a Python Library that allows you to send HTTP/1.1 requests easily.
# Use single quotation marks for defining string
url='https://www.ibm.com/'
r = requests.get(url)
r.status_code:200

# You can view the request body in the following line
# As there is np body for a GET request, we get a None:
print("r.request.headers:", r.request.headers)  # consists of dictionaries
print("r.request.body:", r.request.body)
print("r.headers:", r.headers)
header = r.headers
print("header[date]:", header['date'])
print("header[content-type]:", header['content-type'])
print("header[r.encoding]:", r.encoding)
print("r.status_code:", r.status_code)
print("header[r.text[0:100]:", r.text[0:100])
print("\n")

#######################   GET Request (with URL Parameters) ###############
print("############# GET Request (with URL Parameters)######################\n")
# Create Query string
# Use single quotation marks for defining string
url_get = 'http://httpbin.org/get'
# To create a Query string, add a dictionary.
# The keys are the parameter names
# The values are the value of the Query string:
payload = {"name":"Joseph", "ID":"123"}
# Then passing the dictionary payload to the params parameter of the  get() function:
r = requests.get(url_get, params=payload)
# There is no request body:
print("r.request.body:", r.request.body)
print('r.url:', r.url)
print("r.status_code:", r.status_code)
print("r.headers:", r.headers)
# We can view the response as text:
print("header[r.text[0:100]:", r.text[0:100])
# We can look at the 'Content-Type':
print("header[content-type]:", r.headers['content-type'])
# As the content 'Content-Type' is in the JSON format we can use the method json(), 
# it returns a Python dict:
print("r.json:", r.json())
# The key args has the name and values:
print("r.json:", r.json()['args'])
print("\n")

######################## POST Request ##################################

print("############# POST Request #########################################\n")
# Like a GET request a POST request is used to send data to a server, but the POST request
# sends the data in a request body, not the url. 
# In order to send the Post Request in the URL, we change the route to POST: 
url_post = 'http://httpbin.org/post'

# To make a POST request we use the post() function, 
# the variable payload is passed to the parameter data:
payload = {"name":"Joseph", "ID":"123"}
r_post = requests.post(url_post, data=payload)

# Comparing the URL from the response object of the GET and POST request we see 
# the POST request has no name or value pairs:
print("POST request URL:", r_post.url)
print("GET request URL:", r.url)

# We can compare the POST and GET request body, 
# we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

# We can view the form as well:
print("r_post.json()['form']:", r_post.json()['form'])
print("\n")
# There is a lot more you can do. Check out Requests for more:
# Requests: HTTP for Humans (Title of the document)
# https://requests.readthedocs.io/en/latest/?utm_content=000026UJ&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01&utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_term=10006555




