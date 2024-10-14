####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Reading Files with Open #######
####### B. Ege #######


example1 = "example1.txt"
file1 = open(example1, "r")
print("the file example1 opened!")

print("file1.name:", file1.name)
print("file1.mode:", file1.mode)

# We can read the file and assign it to a variable:
FileContent = file1.read()
print("The file content:\n", FileContent)
print("The file is of type:", type(FileContent))

file1.close
print("The file example1 has been closed!")

########################  A BETTER WAY TO OPEN FILE ####################################

# Using the 'with' statement is better practice, it automatically closes the file even
# if the code encounters an exception

with open(example1, "r") as file1:
    FileContent = file1.read()
    print("The file content:\n", FileContent)

#file1.close

# Verify if the file is closed   
if (file1.closed is True):
    print("The file example1 has been automatically closed!") 
else:
    print("The file example1 has not been automatically closed!") 

# Read first four characters:
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
# Once the method .read(4) is called the first 4 characters are called. 
# If we call the method again, the next 4 characters are called and then 
# 7 characters + the newline

with open(example1, "r") as file1:
    print("file1.read(10):", file1.read(10))
    print("file1.readline(10):", file1.readline(10)) # does not read past the end of line
    print("file1.read(10):", file1.read(10))

# Iterate through the lines
with open(example1,"r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
print("FileasList[1]:", FileasList[1])
print("FileasList[2]:", FileasList[2])
print("FileasList[3]:", FileasList[3])








 

















