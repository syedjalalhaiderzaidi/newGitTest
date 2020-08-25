"""Fibonacci Series
a,b=0,1
while a<100:
    print(a)
    a,b=b,a+b

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words=[]
    for line in story:
        line_words=line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)"""

# Access and modify attributes of an object
class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style,speed):
        self.color = color
        self.style = style
        self.speed=speed

    def accelerate(self):
        self.speed+=5
        print("now speed is: ",self.speed)

     # method 1
    def showDescription(self):
        print("This car is a", self.color, self.style)

    # method 2
    def changeColor(self, color):
        self.color = color
        

c = Car('Black', 'Sedan',120)

# Access attributes
print(c.style)
# Prints Sedan
print(c.color)
# Prints Black
print(c.speed)

# Modify attribute
c.style = 'SUV'
print(c.style)
# Prints SUV
c.accelerate()
# call method 1
c.showDescription()
# Prints This car is a Black Sedan

# call method 2 and set color
c.changeColor('White')

c.showDescription()
print(c.wheels)

    
