####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Lists #######
####### B. Ege #######

# Create a list
L = ["Michael Jackson", 10.1, 1982]
print(L)

# We can use negative and regular indexing with a list:
print('the same element using negative and positive indexing:\n Positive:',L[0], '\n Negative:' , L[-3])
print('the same element using negative and positive indexing:\n Positive:',L[1], '\n Negative:' , L[-2])
print('the same element using negative and positive indexing:\n Positive:',L[2], '\n Negative:' , L[-1])

# Lists can contain strings, floats, and integers. We can nest other lists, and we can also nest tuples
# and other data structures. The same indexing conventions apply for nesting:

L = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
print(L)

# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]

# List slicing
print(L[3:5])

# We can use the method 'extend' to add new elements to the list:
L = ["Michael Jackson", 10.2]
print("L:",L)
L.extend(['pop', 10])
print("L.extend:", L)

# Another similar emthod is 'append'.
# If we apply 'append' instead of 'extend', we add only ONE element to the list:
L = ["Michael Jackson", 10.2]
L.append(['pop', 10])
print("L.apply:",L)

# Each time we apply a method, the list changes. If we apply extend we add two new elements to the list. 
# The list L is then modified by adding two new elements:

# As lists are mutable, we can change them. For example, we can change the first element as follows:
L[0] = "Bon Jovi"
print(L)

# We can also delete an element of a list using the del command:
del(L[2])
print(L)

# We can convert a string to a list using split. For example, the method split translates every group 
# of characters separated by a space into an element in a list:
print("Splitting the string 'hard rock':",'hard rock'.split())

# We can use the split function to separate strings on a specific character which we call a delimiter. 
# We pass the character we would like to split on into the argument, which in this case is a comma. 
# The result is a list, and each element corresponds to a set of characters that have been separated
# by a comma:
print("Splitting the text 'A,B,C,D' by a comma:",'A,B,C,D'.split(','))

############################ COPY & CLONE LIST ###########################
# When we set one variable B equal to A, both A and B are referencing the same list in memory:
A = ["Hard Rock", 10, 1.2]
B = A
print("A:", A)
print("B:", B)
# Initially, the value of the first element in B is set as "hard rock". If we change the first element 
# in A to "banana", we get an unexpected side effect. As A and B are referencing the same list, 
# if we change list A, then list B also changes. If we check the first element of B we get "banana" 
# instead of "hard rock":
print("B[0]:", B[0])
A[0] = "Banana"
print("B[0]:", B[0])

# But you can clone list A by using the following syntax:
B = A[:]
print("Now, B cloned and not copied from A:", B)
# Variable B references a new copy or clone of the original list.
# Now if you change A, B will not change:
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])

################################ QUIZ ON LIST ####################################

# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
a_list = [1, 'hello', [1,2,3], True]

# Retrieve the elements stored at index 1, 2 and 3 of a_list.
print("Elements stored at index 1 to 4 (slicing)",a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2, 1, 'd']
print(A+B)

# Scenario: Shopping list
shopping_list = []
shopping_list = ['Watch','Laptop','Shoes','Pen','Clothes']
shopping_list.append('Football')
# Print the entire shopping list
print("The entire shopping list:", shopping_list[:])
print("The entire shopping list:", shopping_list)
# Print the item that are important to buy from the Shopping List
print("Slicing",shopping_list[1:3])
# Instead of "Pen" I want to buy "Notebook" let's change the item stored in the list. 
shopping_list[3] = "Notebook"
# Let's delete items that are unimportant, such as; I don't want to buy Clothes, let's delete it. 
del(shopping_list[4])
print("After deleting clothes:", shopping_list)


#############################################################################

# You can find the type of an object by using the command type()
type(["a"])
print("type of [a] ist a", type(["a"]))

ratings = [2,5,6,6,8,9,9,10,10]
print("Ratings: ", ratings)
ratings.reverse()
print("ReverseRatings: ", ratings)



















