####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Exception Handling #######
####### B. Ege #######

# EXCEPTIONS
# There are many more exceptions that are built into Python, here is a list of them 
# https://docs.python.org/3/library/exceptions.html

# Now, run each piece of code and observe the exception raised:

# ZeroDivisionError
# 1/0
# --> in this case, it occurs when you try to divide by zero.

# NameError
# y = a + 5
# --> in this case, it means that you tried to use the variable a when it was not defined.

# IndexError
# a = [1, 2, 3]
# a[10]
# --> In this case, it occured because you tried to access data from a list using an index that
#  does not exist for this list.


"""" !!!!!!!!!! WICHTIG !!!!!!!!!!
a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a/b
    print("Success (1) a= ", a)
except ZeroDivisionError:
    print("The number you provided can't divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except NameError:
    print("You tried to use a variable when it was not defined.")
except: # to catch an unexpected exception
    print("Something went wrong")
else: # 'else' allows one to check if there was no exception when executing the try block.
      # This is useful when we want to execute something only if there were no errors.
    print('Success (2) a= ', a)
finally: # 'finally' allows us to always execute something even if there is an exception or not.
         # This is usually used to signify the end of the try except.
    print("Processing Complete!")
"""



# Practice Exercises

# Exercise 1: Handling ZeroDivisionError
# Imagine you have two numbers and want to determine what happens when you divide one number by the other. 
# To do this, you need to create a Python function called safe_divide. You give this function two numbers, 
# a 'numerator' and a 'denominator'. The 'numerator' is the number you want to divide, and the 'denominator' 
# is the number you want to divide by. Use the user input method of Python to take the values.

# The function should be able to do the division for you and give you the result. But here's the catch: 
# if you try to divide by zero (which is not allowed in math), the function should be smart enough to catch 
# that and tell you that it's not possible to divide by zero. Instead of showing an error, it should return None, 
# which means 'nothing' or 'no value', and print "Error: Cannot divide by Zero.


def safe_divide(numerator, denumerator):
    try:
        result = numerator/denumerator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero.")
        return None
    except:
        print("Fatal error! Please give as input a valid input(1)")    
        return None
    finally:
        print("Processing Complete!!")

try:
    numerator = int(input("Please enter a number to divide: "))
    denumerator = int(input("Please enter a number to be divided: "))
    print("Result: ", safe_divide(numerator, denumerator))
except:
    print("Fatal error! Please give as input a valid input(2)")      

# Exercise 2: Handling ValueError
# Imagine you have two numbers and want to find out what happens when you multiple one number by the other. 
# To do this, you need to create a Python function. You give this function two numbers, a 'number1' and a 'number2'.

# When you use this function, it will take a number as input and attempt to multiply it by 2. 
# The function should show you the multiplication result if you provide a valid integer or float value as input. 
# However, the function will be clever enough to detect the mistake if you accidentally enter something other than 
# a whole number, such as a letter or a decimal. It should kindly inform you with a message saying, 
# 'Invalid input! Please enter an integer or a float value.

# Note:- Test with different input types like using integers, strings, zero, negative values, or other data types 
# to validate error handling!

import math
def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Value Error: Invalid input! Please enter an integer.")
    except:
        print("Fatal error! Please give as input a valid input(3)")    

try:
    number1 = float(input("Enter the value for performing calculation (sqrt):"))
    perform_calculation(number1)
except:
    print("Fatal error! Please give as input a valid input(4)")   


# Exercise 3: Handling Generic Exceptions
# Imagine you have a number and want to perform a complex mathematical task. The calculation requires dividing 
# the value of the input argument "num" by the difference between "num" and 5, and the result has to be stored 
# in a variable called "result".

# You have to define a function so that it can perform that complex mathematical task. The function should handle
# any potential errors that occur during the calculation. To do this, you can use a try-except block. 
# If any exception arises during the calculation, it should catch the error using the generic exception class 
# "Exception" as "e". When an exception occurs, the function should display "An error occurred during calculation.

# Note:- Test with different input types like using integers, strings, zero, negative values, or other data types 
# to validate error handling!


def Calculation(number):
    try:
        result = number / (number-5)
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by Zero.")    
    except Exception as e:
        print("An error occurred during calculation.")

try:
    number = float(input("Please enter the number: "))
    result2 = Calculation(number)
    print("result:", result2)
except:
    print("Fatal error! Please give as input a valid input(5)")  

# Why is it best practice to have multiple except statements with each type of error labeled correctly?
# In order to know what type of error was thrown and the location within the program
























