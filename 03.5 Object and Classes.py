####### IBM Data Science Professional #######
####### Python for Data Science, AI & Development #######
####### Object and Classes #######
####### B. Ege #######


# Matplotlib is a plotting library for the Python programming language 
# and its numerical mathematics extension NumPy. 
# Import the Library
import matplotlib.pyplot as plt
#%matplotlib inline

# Creating your own types:
# Defining Classes

# Create a class: Circle
# The function init is a constructor.
# It's a special function that tells Python you are making a new class.
# There are other special functions in Python to make more complex classes. 
# The self parameter refers to the newly created instance of the class. 
class Circle(object):

    # Constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


C1 = Circle(10,"red")  # Object constructor

# In Python, we can also set or change the data attribute directly:
C1.color = 'blue'
C1.radius = 15
C1.add_radius(2)
# We can use the 'dir' command to get a list of the object's methods.
# Many of them are default Python methods.
print("dir(C1):", dir(C1))

# Now, we can look at the data attributes of the object
print("C1.color:", C1.color)
print("C1.radius:", C1.radius)

#C1.drawCircle()

##############################################################################

class Rectangle(object):

    # Constructor
    def __init__(self, color, height, width):
        self.height = height
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
    

myRectangle = Rectangle(20,5,'blue')
print("myRectangle.height:", myRectangle.height)
print("myRectangle.width:", myRectangle.width)
print("myRectangle.color:", myRectangle.color)
#myRectangle.drawRectangle()


##############################################################################

# Scenario: Car dealership's inventory management system
class Car:

    # the default color for all vehicles "white"
    color = "white"

    #Constructor
    def __init__(self, speed, km):
        self.speed = speed
        self.km = km
        self.seats = None

    def add_seat_capacity(self, nrOfSeats):
        self.seats = nrOfSeats

    def showProperties(self):
        print("Speed:",self.speed)
        print("km-Stand:",self.km)
        print("Number of seats:",self.seats) 
        print("Color:",self.color)   

# Creating objects
myCar1 = Car(200, 20)
myCar1.add_seat_capacity(5)
myCar1.showProperties()

myCar2 = Car(180, 25)
myCar2.add_seat_capacity(4)
myCar2.color = "red"
myCar2.showProperties()
