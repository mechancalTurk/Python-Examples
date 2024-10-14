####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Loops #######
####### B. Ege #######


# Before we discuss the range object, 
# it is helpful to think of the range object as ordered list.
# IMPORTANT NOTE: While in Python 2.x it returned as a list, in 3.x it returns a range as object. 
# range(10,15) --> [10,11,12,13,14]
print('range(3) means: ', range(3))
print('range(10,15) means: ', range(10,15))

for i in range(0, 8):
    print("range(0,8) bedeutet:", i)

# For loop example
dates = [1982,1980,1973]

for year in dates:
    print(year)

N = len(dates)
print('N: ', N)
for i in range(N):
    print(i, dates[i]) 

# RANGE:
# In Python 3 ist 'range' ein sog. Generator, der die Elemente erst bei Bedarf erzeugt.
# Vor allem bei Schleifen über eine große Anzahl von Elementen spart das Speicherplatz [KOFLER, S.137]

squares = ["red", "yellow", "green", "purple", "blue"]
print("squares: ", squares)
# Keep in mind: 5 is excluded!
for i in range(0,5):
    squares[i]="white"
print("squares: ", squares)

######################################################
for cnt, square in enumerate(squares):
    print(cnt, square)

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i ,"repetitions to get out of loop.")


################################ QUIZ ON LOOPS #################################
# Write a for loop that prints out all the elements between -5 and 5 using the range function:
# Dikkat! 5 excluded wie bei Slicing.
for i in range(-5,5):
    print('i: ', i)  

# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']. 
# Make sure you follow Python conventions.
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print('Genres2: ', Genre)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    #print("square: ", squares[i]) # Falsch, weil hier die ganze Liste verlangt wird!
    print("square: ", square)

# Write a while loop to display the values of the Rating of an album playlist stored in thePlayListRatings list. 
# If the score is less than 6, exit the loop. The list PlayListRatings is given by: 

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
N = len(PlayListRatings)
#print("Die Länge des PlayLists:", N)
i = 0
while (PlayListRatings[i] >= 6) and (i < N-1):
    print(PlayListRatings[i])
    i = i + 1
    #print("i",i)

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
# Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

N = len(squares)
i = 0
while (squares[i] == "orange") and (i < N-1):
    new_squares.append(squares[i])
    i = i + 1

print('new_squares: ', new_squares)


# PRACTICE QUIZ

# Question 1
# What will be the output of the following:
for x in range(0,3):     
    print(x)

# Question 2
# What is the output of the following:
for x in ['A','B','C']:
    print(x+'A')

# Question 3
# What is the output of the following:
for i,x in enumerate(['A','B','C']):    
    print(i,x)

































