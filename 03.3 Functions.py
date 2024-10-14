####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Functions #######
####### B. Ege #######

# In Python ist es nicht erlaubt, dass mehrere Function denselben Namen haben.
# Diese Regel klingt selbstverständlich; tatsächlich unterstützen viele Programmiersprachen
# wie Java gleichnamige Funktionen, wenn diese sich in ihrer Parameterliste unterscheiden (Overloading) 

# sum()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print("album_ratings:", album_ratings)
print("Die Länge:", len(album_ratings))
print("Die Summe der Elemente im album_ratings[]", sum(album_ratings))

# String Concatenation
vorname="Börtecin"
familienname="Ege"
print("String concatenation:", vorname + " " + familienname)

# Die Verwendung von return in Python-Functions ist optional!
# If there is no return statement, the function returns 'None'. 
# The following two functions are equivalent:
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# sorted() vs. sort()
# sorted is a function and returns a new list, it does not change the original list
print("album_rating: ", album_ratings)
print("sorted_album_rating: ", sorted(album_ratings))

# What is the value of list L after the following code segment is run  :
L = [1,3,2]
print("L before using .sorted(): ", L)
new_L = sorted(L)
print("L after using .sorted() (the original list doesn't change by using .sorted, now only sorted):", new_L)  # als eine neue Liste!

# But sort() changes the original list
lst = list('Hello, World!')
print("lst:",lst)
lst.sort
print("lst.sort (But sort() changes the original list): ", lst)

# A function can multiple also the sequences:
def Mult(a,b):
    c=a*b
    return c
print(Mult(3, 'Michael Jackson '))

######################################################################################################

# Es ist erlaubt, in Functions Loops zu verwenden:
def printStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is", s)

album_ratings = [10.0, 8.5, 9.5]
printStuff(album_ratings)   

# Collecting arguments
# Consider the following function; the function has an asterisk on the parameter names.
# When we call the function, three parameters are packed into the tuple names.
# We then iterate through the loop; the values are printed out accordingly. 
# When the number of arguments are unknown for a function, 
# they can all be packed into a tuple as shown:
def ArtistNames(*names):
    for name in names:
        print(name)

print("When the number of arguments are unknown for a function, they can all be packed into a tuple by (*names) as shown:")
ArtistNames("Michael Jackson", "Roxset", "Frank Sinatra")

# Similarly, The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

print("Similarly, The arguments can also be packed into a dictionary y (**args) as shown:")
printDictionary(Country='Canada',Province='Ontario',City='Toronto')


# Global Variables
# Achtung! In der Praxis wird das Schlüsselwort global möglichst vermieden, 
# weil es oft zu unübersichtlichem Code führt. Stattdessen ist es i.d.R. besser, 
# das Funktionsergebnis mit return zurückzugeben und dann zu speichern.


# Quiz on Functions
def div(x, y):
    return (x/y)

def con(a, b):
    return(a + b)

print(con(2, 2))
print(con('Börtecin', 'Ege'))

# Can the con function we defined before be used to concatenate lists or tuples?
# Answer: Yes
print(con(['a', 'b', 'c'], ['d', 1]))

def Print(A):   
 for a in A: 
    print(a+'1')
Print(['a','b','c'])



