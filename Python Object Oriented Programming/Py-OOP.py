# Python Object Oriented Programming

'''
Within python, everything is an object.
An object is an instance of a class, whereas a class is a blueprint

Classes have methods, which are basically functions you can run on your objects EG:
'''

text = 'hello world!'
print(text.upper())

'''
The .upper() is a method. You can tell because it ends in brackets, which looks like a function
call.

Every function requires 'self' to be passed to it, and special methods are surrounded in two underscores
- for example __init__, which runs as soon as you create an object
'''

class Dog:
    def __init__(self, name):
        # These are creating your attributes, or variables
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def bark(self):
        print('bark')

    def add_one(self, x):
        return(x + 1)

# Create an object
d = Dog('Tim')
print(type(d))

# You can also call an attribute like this, or use a "getter" method to return that attr
print(d.name)
print(d.get_name())

# Call the method on the object
d.bark()
print(d.add_one(5))

# Modify attributes
d.set_name("Ally")
print(d.get_name())


print('-'*20)

'''
Getter and setter methods are really powerful, allowing you to store info in the object and
manipulate it as you go.
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

        # You can also create attributes that aren't passed in, like creating standard variables
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True

        return False

    def get_average_grade(self):
        value = 0

        for student in self.students:
            value += student.get_grade()

        return (value/len(self.students))

s1 = Student('Tom', 19, 95)
s2 = Student('Alice', 19, 75)
s3 = Student('Cara', 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students)
print(course.students[0].name)

print(course.get_average_grade())

print('-'*30)

'''
Inheritance is when you have two classes that are very similar.
You instead create a class that shares all their functionality and implement them as children of the
new class.

In the below example, even without an init in the child classes, you can still run the parent
init and methods
'''

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

    def speak(self):
        print('Hello')

class Cat(Pet):
    def __init__(self, name, age, color):
        # This lets you run the init method of the parent class when you create the child class
        super().__init__(name, age)

        self.color = color

    def speak(self):
        print('meow')

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')

class Dog(Pet):

    def speak(self):
        print('woof')

p = Pet("Sarah", 19)
p.show()
p.speak()

c = Cat('Chris', 34, 'green')
c.show()
c.speak()

d = Dog('Liam', 23)
d.show()
d.speak()

print('-'*20)

'''
Class methods and class attributes. These apply to a class, not an instance of it
'''

class Person:
    # This is a class attribute. It doesn't use SELF and doesn't change with every instance of class
    number_of_ppl = 0

    # CLASS CONSTANT
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name

        # You can call classmethods in the init
        Person.add_person()

    # Class method - These requre the '@classmethod' decorator too and CLS instead of SELF
    @classmethod
    def number_of_people(cls):
        return(cls.number_of_ppl)

    @classmethod
    def add_person(cls):
        cls.number_of_ppl += 1

p1 = Person('Isla')
print(Person.number_of_ppl)
p2 = Person('Eric')

# These will do the same thing because number_of_ppl isn't attached to an object
# Meaning that you can modify it on the class itself
print(p1.number_of_ppl)
print(Person.number_of_ppl)

print(p2.number_of_ppl)
print(p1.number_of_ppl)

print(Person.number_of_people())

print('-'*20)

'''
Static methods are methods that you can call at any time, even if you don't have an object created
They don't have access to an object, so they can't change anything
They need the decorator, but don't need SELF or CLS as they aren't accessing those

This is often how imported modules will run
'''

class Math:

    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def add10(x):
        return x+10

    @staticmethod
    def pr():
        return('hi')

# This doesn't need a Math object to run

print(Math.add5(5))
print(Math.add10(2))
print(Math.pr())
