####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Writing Files with Open #######
####### B. Ege #######


#####################   WRITING FILES with OPEN ############################

Lines = ["Hello world-1!\n","Hello world-2!\n","Hello world-3!\n"]

# Reading from a list
example2 = "example2.txt"
with open(example2,"w") as File1:
    for line in Lines:
        File1.write(line)

# At the end of the loop the file will be automatically closed.
        

# Reading from a file:
with open("example1.txt","r") as readfile:
    # Note that setting the mode to 'w' overwrites all the existing data in the file.
    with open("example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)


# Appending data to an exisiting file
with open("example3.txt","a") as File1:
    File1.write("\n")
    File1.write("End of file\n")

# You can check the file to see if your results are correct: 
with open("example3.txt","r") as File1:
    # readline reads line for line
    # print(File1.readline())
     print(File1.read())

################################# ADDITIONAL MODES #######################################
     
# It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines. 
# Luckily we can access the file in the following modes:
# r+ : Reading and writing. Cannot truncate the file (to bytes of size xx).
# w+ : Writing and reading. Truncates the file (to bytes of size xx), however, opening a file in w+ 
# overwrites it and deletes all pre-existing data.
# a+ : Appending and Reading. Creates a new file, if none exists. 
# You dont have to dwell on the specifics of each mode for this lab.
# .tell() - returns the current position in bytes
# .seek(offset, from) - changes the position by 'offset' bytes with respect to 'from'. 'from' can take
# the value of 0,1,2 corresponding to beginning, relative to current position and end.

with open("example3.txt", "a+") as testwritefile:

    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):
        # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    # move 0 bytes from beginning
    testwritefile.seek(0,0)

    print("\nNew Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

with open('example3.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())

# To work with a file on existing data, use r+ and a+. 
# While using r+, it can be useful to add a .truncate() method at the end of your data. 
# This will reduce the file to your data and delete everything that follows.
with open('example3.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    

###################################  COPY A FILE ######################################

# Copy the file example3.txt to the file example4.txt
with open("example3.txt","r") as readfile:
     with open("example4.txt","w") as writefile:
          for line in readfile:
              writefile.write(line)

# Verify if the copy is successfully executed:
with open("example4.txt","r") as testwritefile:
            print(testwritefile.read())
# After reading files, we can also write data into files and save them in different file formats like .txt, 
# .csv, .xls (for excel files) etc.
            
##################################### EXERCISE  #######################################

# csv — CSV File Reading and Writing
# https://docs.python.org/3/library/csv.html
            
# Your local university's Raptors fan club maintains a register of its active members on a .txt document. 
# Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
# Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. 
# Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
# Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.          

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
'''

with open("members.txt","r+") as readFile:
    with open("inactive.txt","a+") as writeFile:
        readFile.seek(0)
        #print(readFile.read())
        # liest alles in die Liste 'members' 
        members = readFile.readlines()
        #print("Liste members[]:",members)
        #remove header
        header = members[0]
        # liest das Element in der Liste an der Position n und entfernt es
        members.pop(0)
        #print(members)

        inactive=[]
        for member in members:
            if 'no' in member:
              inactive.append(member)

#print("Inactive members:", inactive)
        # come to the top of the file again 
        readFile.seek(0)
        # write header to the top     
        readFile.write(header)
        for member in members:
            if (member in inactive):
                writeFile.write(member)
            else:
                readFile.write(member)      
        readFile.truncate()   
        # truncate([size]) löscht in der Datei alle Daten, die hinter der aktuellen 
        # Schreib-/Leseposition stehen, bzw. – sofern angegeben – alles außer den ersten size Bytes.       



