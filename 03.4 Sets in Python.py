####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Sets #######
####### B. Ege #######

################### SETS
# Work with sets in Python, including operations and logic operations.
# A set is a unique collection of objects in Python. 
# You can denote a set with a pair of curly brackets {}. 
# Python will automatically remove duplicate items:
# Create a set
set1 = {"pop","rock","soul","hard rock","rock","R&B","rock","disco"}
print("set1:",set1)

# Converting a list to a set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop", "Pop", "Rock", "Pop", "Rock", "Rock","R&B", 46.0, 65, "30-Nov-82", None, 10.0]
print(set(album_list))

#### SET OPERATIONS
A = set(["Thriller", "Back in Black", "AC/DC"])
print("Set A:",A)
A.add("NYC")
print("After adding the element NYC:", A)
# If we add the same element twice, nothing will happen as there can be no duplicates in a set:
A.add("NYC")
print("After adding the element NYC again:", A)
A.remove("NYC")
print("After removing the element NYC:", A)

# Verify if the element is in the set
result = "NYC" in A
print("Ist NYC im Set immer noch vorhanden?",result)

# Sets Logic Operations
# Remember that with sets you can check the difference between sets, as well as 
# the symmetric difference, intersection, and union:
# Consider the following sets:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print("album_set1:", album_set1)
print("album_set2:", album_set2)

# Find the intersections
intersection = album_set1 & album_set2
print("Intersection of them:",intersection)
intersection = album_set1.intersection(album_set2) 
print("Intersection of them:",intersection)

# Find the difference in set1 but not set2
print("Find the difference in set1 but not set2:", album_set1.difference(album_set2))

# Find the difference in set2 but not set1
print("Find the difference in set2 but not set1:", album_set2.difference(album_set1))

# Find the union of two sets
print("The union of two sets:",album_set1.union(album_set2))

# Check if subset
result = set(album_set2).issubset(album_set1) 
print("is album_set1 a subset from album_set2?",result)
result = set(album_set1).issubset(album_set2) 
print("is album_set2 a subset from album_set1?",result)

# Check if superset
result = set(album_set1).issuperset(album_set2)  
print("Is album_set1 a superset from album_set2?",result)
result = set(album_set2).issuperset(album_set1)  
print("Is album_set2 a superset from album_set1?",result)

B = set(["Thriller"])
print("The new set B:",A)
result = set(B).issubset(album_set1) 
print("is set B a subset from album_set1",result)
result = set(B).issubset(album_set2) 
print("is set B a subset from album_set2",result)
result = set(album_set1).issuperset(B) 
print("is set album_set1 the superset of B",result)


#### QUIZ ###############
# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1] 
B = set([1, 2, 2, 1])
print("The sum of the list A:", sum(A))
print("The sum of the set B:", sum(B))













