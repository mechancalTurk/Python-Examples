####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Dictionaries #######
####### B. Ege #######


#################### DICTIONARIES #####################
# Das folgende Beispiel zeigt ein Mini-Wörterbuch als Python-Dictionary:
# myDictionary = {'sun':'Sonne', 'moon':'Mond', 'star':'Stern'}
# Zwischen den zwei Komponenten eines Paares steht ein Doppelpunkt.
# Der Ausdruck vor dem Doppelpunkt wird als Key bezeichnet, der dahinter als Value
# <Key>:<Value>


Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print("myDictionary:", Dict)

print("key1:", Dict["key1"])
print("key2:", Dict["key2"])
print("key3:", Dict["key3"])
print("key4:", Dict["key4"])
print("key5:", Dict["key5"])

# Access to the value by the key
print("The value of key1:", Dict["key1"])
print("The value of key2:", Dict["key2"])
print("The value of key3:", Dict["key3"])
print("The value of key4:", Dict["key4"])
print("The value of key5:", Dict["key5"])
print("The value of (0,1):", Dict[(0,1)])

# Each key is separated from its value by a colon ":". 
# Commas separate the items, and the whole dictionary is enclosed in curly braces. 
# An empty dictionary without any items is written with just two curly braces, like this "{}".
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print("release_year_dict:", release_year_dict)
print("In welchem Jahr wurde der Film The Bodyguard gedreht?:", release_year_dict["The Bodyguard"])
# In summary, like a list, a dictionary holds a sequence of elements. 
# Each element is represented by a key and its corresponding value. 
# Dictionaries are created with two curly braces containing keys and values separated by a colon. 
# For every key, there can only be one single value, however, multiple keys can hold the same value.
# Keys can only be strings, numbers, or tuples, but values can be any data type.
# It is helpful to visualize the dictionary as a table, as in the following image. 
# The first column represents the keys, the second column represents the values.

# Get all the keys in dictionary:
print("Get all the keys in dictionary:", release_year_dict.keys())
# Get all the values in dictionary:
print("Get all the values in dictionary:", release_year_dict.values())
# Append value with key into dictionary:
release_year_dict["Graduation"] = 2007
print("After appending the key Graduation:", release_year_dict)
# Delete entries by key:
del(release_year_dict['Thriller']) 
del(release_year_dict["Graduation"])
print("After deleting the keys 'Thriller' and 'Graduation':", release_year_dict)

# Verify the key is in the dictionary
result = "The Bodyguard" in release_year_dict
print("Ist der Film The Bodyguard im Dictionary vorhanden?", result)

#########################   QUIZ ON DICTIONARIES ###########################



















