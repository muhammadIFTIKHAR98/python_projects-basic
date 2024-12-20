#OOPS 

#1. Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

#Answer
'''
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.pi*radius*radius
        self.circumference = Circle.pi*radius*2

radius = int(input("write any radius of circle: "))
Circle(radius)
Area = Circle(radius).area
Circumference = Circle(radius).circumference
print(f"for the radius {radius}. circle area will be {Area} and the circumference will be {Circumference}")   
'''




#2. Write a Python program to create a person class. Include attributes like name, 
# country and date of birth. Implement a method to determine the person's age.

#Answer
'''
from datetime import date   # Import the date class from the datetime module to work with dates

class person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -=1
        return age
    
person1 = person("Simon", "UK", date(1900, 8, 15))
person2 = person("Osama", "USA", date(1963, 5, 12))
person3 = person("Hitler", "Germany/Austria", date(2025, 3, 25))

print("person1")
print("name: ", person1.name)
print("country: ", person1.country)
print("Date of birth: ", person1.date_of_birth)
print("Age: ", person1.calculate_age())

print("person2")
print("name: ", person2.name)
print("country: ", person2.country)
print("Date of birth: ", person2.date_of_birth)
print("Age: ", person2.calculate_age())

print("person3")
print("name: ", person3.name)
print("country: ", person3.country)
print("Date of birth: ", person3.date_of_birth)
print("Age: ", person3.calculate_age())
'''
    
#3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

#Answer
'''
class calculator:
    def __init__(self, number1, number2):
        self.number1 = int(number1)
        self.number2 = int(number2)

    def addition(self):
        self.addition = int(self.number1 + self.number2)
        return self.addition

    def subtraction(self):
        self.subtraction = int(self.number1 - self.number2)
        return self.subtraction

    def multiplication(self):
        self.multiplication = int(self.number1 * self.number2)
        return self.multiplication

    def division(self):
        self.division = (self.number1 // self.number2)
        return self.division



problem1 = calculator(25, 5)
problem2 = calculator(67, 88)
problem3 = calculator(32, 98)

print("problem1")
print("addition: ", problem1.addition())
print("subtraction: ", problem1.subtraction())
print("multiplication: ", problem1.multiplication())
print("division: ", problem1.division())

'''



#4. Write a Python program to create a class that represents a shape. Include methods to calculate 
# its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

#Answer
'''
class shape:
    def __init__(self): #radius, square_side, dimension1, dimension2
        self.radius = radius
        self.square_side = square_side
        self.dimension1 = dimension1
        self.dimension2 = dimension2
    class circle:
        def __init__(self,radius): 
            pi = 3.14
            self.radius = radius
            self.circle_area = pi*self.radius*self.radius
            self.circle_circumference = pi*self.radius*2
    class square:    
        def __init__(self, square_side):
            self.square_side = square_side
            self.sq_area = self.square_side*self.square_side
            self.sq_perimeter = self.square_side + self.square_side
    class rectangle:
        def __init__(self, dimension1, dimension2):
            self.dimension1 = dimension1
            self.dimension2 = dimension2
            self.rec_area = self.dimension1*self.dimension2
            self.rec_perimeter = self.dimension1 + self.dimension2

student1 = shape.circle(5)
student2 = shape.rectangle(2,4)
student3 = shape.square(8)

print("student1")
print("Circle Area: ", student1.circle_area)

print("student2")
print("rectangle Area: ", student2.rec_area)

print("student3")
print("square Area: ", student3.sq_area)
'''

#5. Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

