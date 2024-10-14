####### IBM Data Science Professional #############
####### Python for Data Science, AI & Development #
####### Webscraping ###############################
################### B. Ege ########################


# !pip install html5lib
# !pip install bs4

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

# Beatiful Soup Object
# Beautiful Soup is a Python library for pulling data out of HTML and XML files, 
# we will focus on HTML files. This is accomplished by representing the HTML 
# as a set of objects with methods used to parse the HTML. We can navigate the HTML as a tree, 
# and/or filter out what we are looking for.

# Consider the following HTML:
'''
%%html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
'''

# We can store it as a string in the variable HTML:
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# To parse a document, pass it into the BeautifulSoup constructor. 
# The BeautifulSoup object represents the document as a nested data structure:
#soup = BeautifulSoup(html,'html5lib') --> returns error!!!
soup = BeautifulSoup(html,'html.parser') # now, it works.

# First, the document is converted to Unicode (similar to ASCII) and HTML entities are converted 
# to Unicode characters. Beautiful Soup transforms a complex HTML document into a complex tree 
# of Python objects. The BeautifulSoup object can create other types of objects. 
# In this lab, we will cover BeautifulSoup and Tag objects, that for the purposes of this lab 
# are identical. Finally, we will look at NavigableString objects.

# We can use the method prettify() to display the HTML in the nested structure:
print(soup.prettify())

tag_object = soup.title
print("tag object:", tag_object)
print("tag object type:",type(tag_object))
# If there is more than one Tag with the same name, the first element with that Tag name is called. 
# This corresponds to the most paid player:
tag_object=soup.h3
# Enclosed in the bold attribute b, it helps to use the tree representation. 
# We can navigate down the tree using the child attribute to get the name.
print(tag_object)
print("\n")

####################### Children, Parents, and Siblings ####################################

print("*****************Children, Parents, and Siblings******************\n")
# As stated above, the Tag object is a tree of objects. We can access the child of the tag or navigate down the branch as follows:
tag_child = tag_object.b  # b: bold
print("tag_child:", tag_child)

parent_tag = tag_child.parent
print("parent_tag:", parent_tag)
# the result is identical to tag_object
print("tag_object:", tag_object)
# tag_object parent is the body element:
print("tag_object.parent:", tag_object.parent)
# tag_object sibling is the paragraph element:
sibling_1 = tag_object.next_sibling
print("sibling_1:", sibling_1)
sibling_2 = sibling_1.next_sibling
print("sibling_2:", sibling_2)
sibling_3 = sibling_2.next_sibling
print("sibling_3:", sibling_3)
sibling_4 = sibling_3.next_sibling
print("sibling_4:", sibling_4)
sibling_5 = sibling_4.next_sibling
print("sibling_5:", sibling_5)
sibling_6 = sibling_5.next_sibling
print("sibling_6:", sibling_6)

######### HTML ATTRIBUTES ##########

# If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest. 
# You can access a tag's attributes by treating the tag like a dictionary:
print("tag_child['id']:", tag_child['id'])
# We can also obtain the content of the attribute of the tag using the Python get() method:
print("tag_child.get('id'):", tag_child.get('id'))
# You can access that dictionary directly as attrs:
print("tag_child.attrs:", tag_child.attrs)
print("tag_child.string:", tag_child.string)
print("type", type(tag_child.string))

# A NavigableString is similar to a Python string or Unicode string. 
# To be more precise, the main difference is that it also supports some BeautifulSoup features. 
# We can convert it to string object in Python:
unicode_string = str(tag_child.string)
print("unicode_string:", unicode_string)

############# FILTERS #############

# Filters allow you to find complex patterns, the simplest filter is a string. 
# In this section we will pass a string to a different filter method and Beautiful Soup will 
# perform a match against that exact string. Consider the following HTML of rocket launches:

'''
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>
'''
print("\n")
# We can store it as a string in the variable table:
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
# table_bs = BeautifulSoup(table, 'html5lib') # --> returns error!!!
table_bs = BeautifulSoup(table, 'html.parser') 

table_rows = table_bs.find_all('tr')
print(table_rows)
print("\n")
first_row = table_rows[0]
print("first row:", first_row)
print("type first row:", type(first_row))
print("We obtain the child:", first_row.td)
print("\n")

for i,row in enumerate(table_rows):
    print("row",i,"is",row)
print("\n")

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
print("\n")

###################  ATTRIBUTES ####################

# If the argument is not recognized it will be turned into a filter on the tag's attributes. 
# For example with the id argument, Beautiful Soup will filter against each tag's id attribute. 
# For example, the first td elements have a value of id of flight, therefore we can filter based on that id value.
print(table_bs.find_all(id="flight"))
# We can find all the elements that have links to the Florida Wikipedia page:
print(table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida"))
# If we set the href attribute to True, regardless of what the value is, the code finds all tags with href value:
print("all the elements with href value", table_bs.find_all(href=True))
# find all the elements without href value
print("find all the elements without href value:", table_bs.find_all(href=False))
print("\n")
# Using the soup object soup, find the element with the id attribute content set to "boldest".
print(soup.find_all(id='boldest'))
# With string you can search for strings instead of tags, where we find all the elments with Florida:
print(table_bs.find_all(string="Florida"))

# find()
# The find_all() method scans the entire document looking for results. It’s useful if you are looking for one element, 
# as you can use the find() method to find the first element in the document.
print(table_bs.find(string="Florida"))

# Scraping tables from a Web page using Pandas
# The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
import pandas as pd
print("tables:", pd.read_html(url))


# See also in the Lab:
# Downloading And Scraping The Contents Of A Web Page
# Scrape all images Tags
# Scrape data from HTML tables


print("\n")


