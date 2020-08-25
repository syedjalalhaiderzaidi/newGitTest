"""
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist=[1,2,3,4]
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


# base class
class Vehicle():
    def __init__(self, color):
        self.color = color
    def description(self):
        print("I'm a", self.color, "Vehicle")

# subclass
class Car(Vehicle):
    def __init__(self, color, style):
        super().__init__(color)    # invoke Vehicle’s __init__() method
        self.style = style
    def description(self):
        print("I'm a", self.color, self.style)

# create an object from each class
v = Vehicle('Red')
c = Car('Black', 'SUV')

v.description()
# Prints I'm a Red Vehicle
c.description()
# Prints I'm a Black SUV

# base class 1
class GroundVehicle():
    def __init__(self, color):
        self.color=color
    def drive(self):
        print("Drive me on the road!")
    def description(self):
        print("I am a ",self.color,"ground vehicle")
            

# base class 2
class FlyingVehicle():
    def __init__(self, color):
        self.color=color
    def fly(self):
         print("Fly me to the sky!")
    def description(self):
        print("I am a ",self.color,"flying vehicle")

    def wings(self):
        print("I have 2 wings")

# subclass
class FlyingCar(GroundVehicle, FlyingVehicle):
    def __init__(self,color,style):
        super().__init__(color)
        self.style=style

    def description(self):
        print("I am a ",self.color,"flying",self.style)

# create an object of a subclass
fc = FlyingCar("Black","SUV")
gv=GroundVehicle("Red")
fv=FlyingVehicle("Blue")
fc.drive()
# Prints Drive me on the road!
fc.fly()
fc.description()
gv.description()
fv.description()
fc.wings()
fv.wings()

# Prints Fly me to the sky!
"""
"""
import os
os.rename("foo.txt","change.txt")

fo = open("foo.txt", "r+")
#fo.write( "Python is a great language.\nYeah its great!!\n")
#str = fo.read(15);
#print ("Read string from file is: ",str)
fo.seek(10)
position = fo.tell()
print ("Current file position : ", position)
print(fo.readline())
fo.close()
"""
