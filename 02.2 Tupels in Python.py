####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Tupels #######
####### B. Ege #######

# TUPLES
# In Python, there are different data types: String, Integer, and Float.
# These data types can all be contained in a tuple.
# In einem Tupel sind mehrere Objekte eventuell unterschiedlicher Typen zu einem komplexen
# Objekt zusammengefasst. Von der Idee her wird bei einem Tupel die Modellierung der
# Struktur eines komplexen Einzelobjektes betont, während man bei einer Liste eher an die
# Aufzählung vieler Einzelobjekte denkt. 
# Typische Tupel aus dem Alltag sind:
# Name und Geburtsdatum einer Person
# Adresse als Tupel mit fünf Elementen (Name, Straße, HausNr, PLZ, Stadt)
# Beschreibung einer Farber durch Angabe von Rot-, Grün, und Blaukomponente

# Formel besteht ein Tupel bei Python aus einer Folge von Objekten ev. unterschiedlicher 
# Typen, diedurch Komma getrennt sind. Sie können (aber müssen nicht) in runden Klammern stehen.


tuple1 = ("disco", 10, 1.2)
print(tuple1)

print("The type of the variable tuple1 is:", type(tuple1))

# INDEXING
# Each element of a tuple can be accessed via an index. 
# We can also use negative indexing (also wie in den Listen). 
# Achtung! Die negative indexing fängt immer bei -1 an!
print("Negative Indexing:", tuple1[-1])
print("Negative Indexing:", tuple1[-2])
print("Negative Indexing:", tuple1[-3])


# CONCATENATE TUPLES
# We can concatenate or combine tuples by using the + sign:
tuple2 = tuple1 + ("hard rock", 10)
print("Concatenation of two tuples:", tuple2)

# SCLICING
print(tuple2[3:5])
print("Länge des Tupels:", len(tuple2))

# SORTING
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
print("Ratings:", Ratings)
print("sorted Ratings:", sorted(Ratings))

# NESTED TUPLE
# A tuple can contain another tuple as well as other more complex data types. 
# This process is called 'nesting'. 
# 
# Consider the following tuple with several elements:
NestedT = (1,2,("pop","rock"),(3,4),("disco",(1,2)))
print("The NestedT tuple:",NestedT)
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# We can use the second index to access the nested tuples, e.g:
print("Element 2,0 of NestedT Tuple: ", NestedT[2][0])
print("Element 2,1 of NestedT Tuple: ", NestedT[2][1])

# 3. Elementin ikinci elemaninin ilk elemani:
print("3. Elementin ikinci elemaninin ilk elemani:", NestedT[2][1][0])

# 5. Elementin ikinci elemaninin ikinci elemaninin ilk elemani:
print("5. Elementin ikinci elemaninin ikinci elemaninin ilk elemani:", NestedT[4][1][0])

##################### QUIZ ON TUPLES ##################
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco")
print(genres_tuple)
# Find the index of 's' in "disco":
print("The index of 's' in 'disco':", genres_tuple[7][2])





