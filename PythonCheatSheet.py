#Python Cheat sheet

#single comment

'''
Multi Line Comment
'''

#import modules
import random
import sys
import os

#Hello World
print('Hello World')

#variables
name = 'john'
print(name)

'''
Data Types
- Numbers
- String
- List
- Tuple
- Dict
'''

#Mathematical operators
#Order of operations matter
print("5 + 2 = ", 5+2)
print("5 - 2 = ", 5-2)
print("5 * 2 = ", 5*2)
print("5 / 2 = ", 5/2)
print("5 % 2 = ", 5%2)
print("5 ** 2 = ", 5**2)
print("5 // 2 = ", 5//2)

quote = "\"Always remember you are unique"

multi_line_quote = ''' Just
like everyone else'''

#string concatenation and multiplication
print("%s %s %s" % ('Replacement', quote, multi_line_quote))
print ("\n" * 5)

#Lists
grocery_list = ['juice', 'tomato', 'potato',
				'potato']

print(grocery_list[0])

#Changing values
grocery_list[0] = 'green juice'
print(grocery_list[0])

#print a range from the list
print(grocery_list[1:3])

other_events = ['wash car', 'cash check']
#2d arrays
to_do_list = [other_events, grocery_list]
print(to_do_list)

#print from 2d lists
print(to_do_list[1][1])

#add items
grocery_list.append('onions')
print(grocery_list)

#insert in the middle
grocery_list.insert(1, "Pickle")

#remove from list
grocery_list.remove("tomato")

print(grocery_list)


#sort list
grocery_list.sort()
print(grocery_list)

grocery_list.reverse()
print(grocery_list)

del grocery_list[4]
print(grocery_list)

#combined lists
to_do_list2 = other_events + grocery_list

#length of list, last and first alphabetically
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

#Tuple
#A list that can't be changed after it's made

pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
print(new_tuple)
new_list = tuple(new_tuple)

#length. Min and Max works here too
print(len(new_list))

#Dictionarys/Maps
#Keys and values

super_villains = {'Fiddler': "Isaac Bowin",
					'Captain Cold': 'Leonard Snart',
					'Weather Wizard': 'Mark Mardon',
					'Mirror Master' : 'Sam Scudder',
					'Pied Piper': 'Thomas Peterson'}

#get single value
print(super_villains['Captain Cold'])

#delete entry
del super_villains['Fiddler']

#update
super_villains["Pied Piper"] = "Hartley Rathaway"

print(len(super_villains))

print(super_villains.get("Pied Piper"))

print(super_villains.keys())
print(super_villains.values())

# Conditionals

age = 21

'''
if age > 16:
	print('You are old enough to drive')
else :
	print ('You are not old enough to drive')
'''

if age >= 21:
	print("You are old enough to drive a tractor")
elif age >= 16:
	print('You are old enough to drive a car')
else:
	print ('You are not old enough to drive')

#logical operators
if ((age >=1) and (age <=18)):
	print('You get a birthday')
elif (age == 21) or (age >= 65):
	print('You get a birthday')
elif not(age == 30):
	print('You dont get a birthday')
else:
	print("You get a birthday party")

# Loops

for x in range(0, 10):
	print(x, " ", end="")

#looping through a list
for y in grocery_list:
	print(y)

#defining a list in the for loop
for x in [2,4,6,8,10]:
	print(x)

#looping in 2d arrays
num_list = [[1,2,3], [4,5,6], [7,8,9]]

for x in range(0,3):
	for y in range(0,3):
		print(num_list[x][y])

#while loop
#Good for when you don't know how long you need to loop for

random_num = random.randrange(0,100)

while (random_num != 15):
	print(random_num)
	random_num = random.randrange(0,100)

i = 0

while(i <= 20):
	if(i%2 == 0):
		print(i)
	elif(i == 9):
		break
	else:
		i += 1
		continue

	i += 1

# functions
#Define them before you use/call them
#variables created inside a function doesn't exist outside it (sumNum in this instance)
def addNumber(first_num, last_num):
	sumNum = first_num + last_num
	return sumNum

#call the function and print what's returned
print(addNumber(1,4))

#Another version of user input using the system StandardIn class
print('What is your name?')
name = sys.stdin.readline()

print("Hello", name)

#strings and substrings
long_string = "I'll catch you if you fall - The Floor"

#get parts of a string
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])

#string contatenation
print(long_string[:4] + "be there")
print("%c is my %s letter and my number %d number is %.5f" % 
	('X', 'favourite', 1, 0.14))

print(long_string.capitalize())

#Where in the string is a part located
print(long_string.find("Floor"))

print(long_string.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("Floor", "Ground"))

#clear whitespace
print(long_string.strip())

#split into list
quote_list = long_string.split(" ")
print(quote_list)

# file IO

test_file = open('test.txt', "wb")
print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Write me to the file\n", "UTF-8"))

test_file.close()

#open file in read mode, save contents to variable, and print
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)

#delete file
os.remove("test.txt")

#Objects/OOP

#attributes with __ preceding them are set to Private
#These need to be manipulated with getter and setter methods
#using only a single underscore will set them to "protected", which allws the child classes to reach the getters and setters

class Animal:
	__name = None
	__height = 0
	__weight = 0
	__sound = 0

	#constructor method
	#This runs when an object is created and tells the code to give 
	#the object all the relevant attributes
	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound

	def set_name(self, name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height):
		self.__height = height

	def get_height(self):
		return self.__height

	def set_weight(self, weight):
		self.__weight = weight

	def get_weight(self):
		return self.__weight

	def set_sound(self, sound):
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} KG and says {}".format(self.__name, 
															self.__height, 
															self.__weight, 
															self.__sound)

#Create the object
cat = Animal("Whiskers", 33, 10, "Meow")

print(cat.toString())

#Inheritance
#This allows you to create a second class with all the info of the parent clas

class Dog(Animal):
	__owner = ""

	#child constructors set the attrs of the parent as well as the child
	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner

		#this super allows you to run the constructor of the parent instead of rewriting the same code
		super(Dog, self).__init__(name, height, weight, sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return self.__owner

	def get_type(self):
		print("Dog")

	def toString(self):
		return "{} is {} cm tall and {} KG and says {}. How owner is {}".format(self._Animal__name,
                                                               				self._Animal__height,
                                                               				self._Animal__weight,
                                                               				self._Animal__sound,
																			self.__owner)

	#method overloading
	def multiple_sounds(self, how_many=None):
		if how_many is None:
			print(self.get_sound())
		else:
			print(self.get_sound() * how_many)

#create dog object
spot = Dog("Spot", 53, 27, "Ruff", "John")
print(spot.toString())

#polymorphism
class AnimalTesting:
	def get_type(self, animal):
		animal.get_type()

test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()




