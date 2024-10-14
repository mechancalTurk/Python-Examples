
####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Practice Lab #######
####### B. Ege #######


# SCENARIO: TEXT ANALYSIS

#Press Shift+Enter to run the code

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer(object):
    
    
    # Inside the constructor,we will convert the text argument to lowercase using the lower() method.
    # Then, will Remove punctuation marks (periods, exclamation marks, commas, and question marks) from 
    # the text using the replace() method. At last, we will Assign the formatted text to a new attribute called fmtText.
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        # defining a new attribute called fmtText
        self.fmtText = formattedText

    # In this step, we will Implement the freqAll() method with the below parameters:
    # Split the fmtText attribute into individual words using the split() method.
    # Create an empty dictionary to store the word frequency.
    # Iterate over the list of words and update the frequency dictionary accordingly.
    # Use count method for counting the occurence
    # Return the frequency dictionary.
    def freqAll(self):  

        # split text into words
        wordList = self.fmtText.split(' ')
        print("wordList: ", wordList)
        print("Count of 'lorem'", wordList.count("lorem"))
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
        # A set is a unique collection of objects in Python. 
        # You can denote a set with a pair of curly brackets {}. 
        # Then Python will automatically remove duplicate items!
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


# Step-1: Create an instance of TextAnalyzer Class
# Instantiate teh TextAnalyzer class by passing the given string as an argument
analyzed = TextAnalyzer(givenstring)

# Step-2: Call the function that converts the data into lowercase
print("Formatted Text:", analyzed.fmtText)

# Step-3: Call the function that counts the frequency of all unique words from the data.
freqMap = analyzed.freqAll()
print("The content of the dictionary freqMap: ", freqMap)

# Step-4: Step-4 Call the function that counts the frequency of specific word
# Here, we will call the function that counts the frequency of the word "lorem" 
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")


# EXAM
# Write a function name add that takes two parameter a and b, then return the output of  a + b 
# (Do not use any other variable! You do not need to run it. Only write the code about how you define it.)
def add(a, b):
    return (a+b)
result=add(76,1)
print("76+1 is:",result)








