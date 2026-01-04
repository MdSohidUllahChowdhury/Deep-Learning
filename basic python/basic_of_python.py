# Welcome to Your Comprehensive Python Learning File!
# This file is designed to be a one-stop guide, from the absolute basics to advanced Python concepts.
# Each section includes explanations and runnable code examples.

# To run a piece of code, you can copy it into a separate Python file and run it,
# or run this file and see the output.

print("--- Starting Your Python Journey! ---")

# ==============================================================================
# Part 1: Python Basics
# ==============================================================================

print("\n--- Part 1: Python Basics ---")

#! --- 1.1 Syntax and Comments ---
# Python's syntax is known for being clean and readable.
# It uses indentation (usually 4 spaces) to define code blocks, instead of brackets.

# This is a single-line comment.

"""
This is a
multi-line comment, often used for docstrings
at the beginning of functions or modules.
"""

#! --- 1.2 Variables and Data Types ---
# Variables are containers for storing data values.
# Python is dynamically typed, so you don't need to declare the type of a variable.

# String (text)
a_string = "Hello, Python!"
print("String:", a_string)

# Integer (whole number)
an_integer = 10
print("Integer:", an_integer)

# Float (decimal number)
a_float = 3.14
print("Float:", a_float)

# Boolean (True or False)
a_boolean = True
print("Boolean:", a_boolean)

# You can check the type of a variable with the type() function.
print("Type of a_string:", type(a_string))


#! --- 1.3 Type Casting ---
# You can convert between data types.
int_from_float = int(a_float) # will be 3 (truncates, doesn't round)
float_from_int = float(an_integer) # will be 10.0
string_from_int = str(an_integer) # will be "10"

print("Casted int:", int_from_float)
print("Casted float:", float_from_int)
print("Casted string:", string_from_int)


#! --- 1.4 Basic Operators ---
# Arithmetic Operators
x = 10
y = 3
print("x + y =", x + y) # Addition
print("x - y =", x - y) # Subtraction
print("x * y =", x * y) # Multiplication
print("x / y =", x / y) # Division (results in a float)
print("x // y =", x // y) # Floor Division (results in an integer)
print("x % y =", x % y) # Modulus (remainder)
print("x ** y =", x ** y) # Exponentiation

# Comparison Operators
print("x > y is", x > y)   # Greater than
print("x < y is", x < y)   # Less than
print("x == y is", x == y) # Equal to
print("x != y is", x != y) # Not equal to

# Logical Operators
p = True
q = False
print("p and q is", p and q) # and (True if both are True)
print("p or q is", p or q)   # or (True if at least one is True)
print("not p is", not p)     # not (inverts the boolean)


#! --- 1.5 String Manipulation ---
s = "Journey Before Destination"

# Length of a string
print("Length of s:", len(s))

# Indexing (accessing a character) - starts at 0
print("First character:", s[0])
print("Last character:", s[-1])

# Slicing (getting a substring)
print("First 7 characters:", s[0:7]) # from index 0 up to (but not including) 7
print("From index 8 onwards:", s[8:])
print("Last 11 characters:", s[-11:])

# String Methods
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Replace 'Before' with 'after':", s.replace("Before", "after"))
print("Splitting the string by spaces:", s.split(' '))

# Formatted Strings (f-strings) - very useful!
name = "Kaladin"
age = 20
print(f"{name} is {age} years old.")


#! ==============================================================================
#! Part 2: Data Structures
#! ==============================================================================

print("\n--- Part 2: Data Structures ---")

#! --- 2.1 Lists ---
# Ordered, changeable (mutable), and allow duplicate members.
my_list = [1, "apple", 3.14, "apple"]
print("My list:", my_list)

# Access items by index
print("Second item:", my_list[1])

# Change an item
my_list[1] = "banana"
print("List after change:", my_list)

# List methods
my_list.append("orange") # Add to end
print("List after append:", my_list)

my_list.insert(1, "cherry") # Insert at a specific index
print("List after insert:", my_list)

my_list.remove("banana") # Remove the first occurrence of an item
print("List after remove:", my_list)

last_item = my_list.pop() # Remove and return the last item
print("Popped item:", last_item)
print("List after pop:", my_list)

# List comprehensions - a concise way to create lists
squares = [i**2 for i in range(5)] # creates a list of squares from 0 to 4
print("List of squares:", squares)


#! --- 2.2 Tuples ---
# Ordered, unchangeable (immutable), and allow duplicate members.
my_tuple = (1, "apple", 3.14, "apple")
print("My tuple:", my_tuple)
# You can access items, but you can't change them.
# my_tuple[1] = "banana" # This would cause a TypeError


#! --- 2.3 Sets ---
# Unordered, unindexed, and do not allow duplicate members.
my_set = {1, "apple", 3.14}
print("My set:", my_set)
my_set.add("banana")
print("Set after add:", my_set)
# Note: if you add a duplicate, it will be ignored.
my_set.add("apple")
print("Set after adding duplicate:", my_set)


#! --- 2.4 Dictionaries (or Maps) ---
# Unordered (in older Python versions), changeable, and indexed.
# They store data in key:value pairs.
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("My dictionary:", my_dict)

# Access items by key
print("Model:", my_dict["model"])

# Change a value
my_dict["year"] = 2024
print("Dict after change:", my_dict)

# Add a new key-value pair
my_dict["color"] = "red"
print("Dict after adding item:", my_dict)

# Iterate through a dictionary
print("Iterating through keys:")
for key in my_dict:
  print(key)

print("Iterating through values:")
for value in my_dict.values():
  print(value)

print("Iterating through key-value pairs:")
for key, value in my_dict.items():
  print(f"{key}: {value}")

#! --- 2.5 Core Data Structures: List vs. Set vs. Dictionary ---
# These three data structures are the workhorses of Python. Understanding their differences is crucial.
#
# Key Differences Summarized:
#
# Aspect         | List                                    | Set                                     | Dictionary (Map)
# ---------------|-----------------------------------------|-----------------------------------------|---------------------------------------------
# Structure      | Ordered collection of items .            | Unordered collection of unique items.   | Unordered collection of key-value pairs.
# Ordering       | Ordered (maintains insertion order).    | Unordered (does not guarantee order).   | Ordered (since Python 3.7).
# Indexing       | Accessed by numeric index (e.g., `[0]`). | Cannot be indexed.                      | Accessed by key (e.g., `["name"]`).
# Mutability     | Mutable (can be changed).               | Mutable (can be changed).               | Mutable (can be changed).
# Duplicates     | Allows duplicate elements.              | Does NOT allow duplicate elements.      | Does NOT allow duplicate keys.
# Syntax         | `my_list = [1, "a", 1]`                 | `my_set = {1, "a"}`                     | `my_dict = {"key1": 1, "name": "a"}`
#
# --- When to Use Each ---
#
# Use a LIST when:
# - You need an ordered sequence of items.
# - The order matters and you need to access items by their position.
# - You might have duplicate items.
# - Example: A list of steps in a recipe, a leaderboard of scores.
#
# Use a SET when:
# - You need to store a collection of UNIQUE items.
# - Membership testing (checking if an item is in the collection) is a primary concern (it's very fast).
# - You want to perform mathematical set operations (union, intersection, difference).
# - Example: Storing a list of unique user IDs, finding the unique vowels in a word.
#
# Use a DICTIONARY (or MAP) when:
# - You need to store data as key-value pairs.
# - You want to associate specific pieces of information with a unique identifier (the key).
# - You need fast lookups based on a key.
# - Example: Storing a user's profile (name, age, email), representing structured data from a database.
#

#! ==============================================================================
#! Part 3: Control Flow
#! ==============================================================================

print("\n--- Part 3: Control Flow ---")

#! --- 3.1 Conditional Statements ---
# if, elif, else
temperature = 25

if temperature > 30:
  print("It's a hot day!")
elif temperature > 20:
  print("It's a pleasant day.")
else:
  print("It's a cool day.")

#! --- 3.2 Loops ---
# 'for' loop - for iterating over a sequence
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
  print(fruit)

# You can use range() to loop a specific number of times
print("Looping with range:")
for i in range(5):
  print(i) # will print 0, 1, 2, 3, 4

# 'while' loop - continues as long as a condition is true
count = 0
print("While loop:")
while count < 5:
  print(count)
  count += 1 # Important: don't forget to change the condition variable!

# --- 3.3 Loop Control Statements ---
# 'break' - exits the loop
print("Loop with break:")
for i in range(10):
  if i == 5:
    break
  print(i)

# 'continue' - skips the rest of the current iteration and goes to the next
print("Loop with continue:")
for i in range(10):
  if i % 2 == 0: # if i is even
    continue
  print(i)


#! ==============================================================================
#! Part 4: Functions
#! ==============================================================================

print("\n--- Part 4: Functions ---")

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

#! --- 4.1 Defining and Calling a Function ---
def greet():
  print("Hello from a function!")

greet() # Calling the function

#! --- 4.2 Parameters and Arguments ---
def greet_person(name, greeting="Hello"): # 'greeting' has a default value
  print(f"{greeting}, {name}!")

greet_person("Alice") # Uses the default greeting
greet_person("Bob", "Good morning") # Overrides the default

#! --- 4.3 Return Values ---
def add_numbers(x, y):
  return x + y

sum_result = add_numbers(5, 3)
print("Result of add_numbers:", sum_result)

#! --- 4.4 Lambda Functions ---
# A small anonymous function.
# Can take any number of arguments, but can only have one expression.
# lambda arguments: expression
multiply = lambda a, b: a * b
print("Result of lambda multiply:", multiply(5, 6))


#! ==============================================================================
#! Part 5: File Handling
#! ==============================================================================

print("\n--- Part 5: File Handling ---")

# The 'with' statement is the recommended way to handle files,
# as it ensures the file is closed automatically.

# --- 5.1 Writing to a file ---
# 'w' mode will overwrite the file if it exists.
with open("my_learning_file.txt", "w") as f:
  f.write("This is the first line.\n")
  f.write("This is the second line.\n")

# --- 5.2 Reading from a file ---
# 'r' mode is for reading.
with open("my_learning_file.txt", "r") as f:
  content = f.read()
  print("Content of file:\n" + content)

# --- 5.3 Appending to a file ---
# 'a' mode will add content to the end of the file.
with open("my_learning_file.txt", "a") as f:
  f.write("This line was appended.\n")

# Reading again to see the appended line
with open("my_learning_file.txt", "r") as f:
    print("Content after append:\n" + f.read())


# ==============================================================================
# Part 6: Object-Oriented Programming (OOP)
# ==============================================================================

print("\n--- Part 6: Object-Oriented Programming (OOP) ---")

# Object-Oriented Programming is a programming paradigm centered around "objects" rather than functions and logic.
# An object is a self-contained entity that consists of both data (attributes) and procedures (methods).
# OOP is based on four fundamental principles, often called the "four pillars."

# --- Pillar 1: Encapsulation ---
# Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class).
# It restricts direct access to some of an object's components, which is a key principle of data hiding.
# In Python, we use conventions to denote private attributes (e.g., a single underscore `_` prefix).

class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model       # "Protected" attribute (convention)
        self.__speed = 0          # "Private" attribute (name mangling)


    def accelerate(self):
        self.__speed += 10
        print(f"The {self.make} is accelerating. Current speed: {self.__speed} mph.")


    def brake(self):
        if self.__speed > 0:
            self.__speed -= 7
        print(f"The {self.make} is slowing down. Current speed: {self.__speed} mph.")

# The user of the Car object doesn't need to know *how* the speed is managed,
# they just use the `accelerate` and `brake` methods. The `__speed` is encapsulated.
my_car = Car("Tesla", "Model S")
my_car.accelerate()
# print(my_car.__speed) # This would raise an AttributeError, enforcing encapsulation.


# --- Pillar 2: Inheritance ---
# Inheritance is the mechanism by which one class (the "child" or "subclass") can
# inherit the attributes and methods of another class (the "parent" or "superclass").
# This promotes code reuse ("Don't Repeat Yourself").

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

# The Dog class inherits from Animal. It gets the `name` attribute and the `speak` method.
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# The Cat class also inherits from Animal.
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

my_dog = Dog("Buddy")
print(my_dog.speak()) # Output: Buddy says Woof!

my_cat = Cat("Whiskers")
print(my_cat.speak()) # Output: Whiskers says Meow!


# --- Pillar 3: Polymorphism ---
# Polymorphism, from the Greek for "many forms," allows objects of different classes
# to be treated as objects of a common superclass. It's the ability for a method
# to do different things depending on the object it is acting upon.

# We can see polymorphism in action with our Animal classes.
# We can write a function that works with any Animal, and it will behave
# correctly based on the actual type of animal passed to it.

def make_animal_speak(animal):
    print(animal.speak())

# We can pass a Dog or a Cat object to the same function.
make_animal_speak(my_dog)
make_animal_speak(my_cat)

# Another example is the `+` operator. For numbers, it adds. For strings, it concatenates.
# This is a form of polymorphism.
print(1 + 2)       #
print("Hello" + " " + "World")


# --- Pillar 4: Abstraction ---
# Abstraction means hiding complex implementation details and showing only the
# essential features of the object. It's about simplifying a complex system.
# When you drive a car, you don't need to know how the engine works internally.
# You just need to know how to use the steering wheel, pedals, and gear shift.

# In Python, we often use abstract base classes (ABCs) to define a common interface.
from abc import ABC, abstractmethod

class Shape(ABC): # This is now an abstract class
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

# The `Shape` class provides an abstraction. Any class that inherits from `Shape`
# *must* provide its own implementation for `area` and `perimeter`.

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
    def perimeter(self):
        return 4 * self.side_length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

# We can now create objects and use their methods without needing to know the
# complex formulas behind them. The complexity is abstracted away.
my_square = Square(10)
print(f"Square area: {my_square.area()}")

my_circle = Circle(5)
print(f"Circle area: {my_circle.area()}")


# ==============================================================================
# Part 7: Advanced Topics
# ==============================================================================

print("\n--- Part 7: Advanced Topics ---")

# --- 7.1 Error Handling ---
# try, except, else, finally
try:
  # Code that might raise an error
  result = 10 / 0
except ZeroDivisionError:
  # Code that runs if a specific error occurs
  print("Error: Cannot divide by zero!")
except Exception as e:
  # A general catch-all for other exceptions
  print(f"An unexpected error occurred: {e}")
else:
  # Code that runs if no exception occurred
  print("Division was successful.")
finally:
  # Code that runs no matter what
  print("This block always executes.")

# --- 7.2 Modules and Packages ---
# A module is a file containing Python code. A package is a folder of modules.
# You can import code from other files to reuse it.

# Standard library imports
import math
print("Value of Pi:", math.pi)

from datetime import datetime
print("Current time:", datetime.now())

# You can also import from your own Python files.
# If you had a file named 'my_module.py' with a function 'my_func', you could do:
# from my_module import my_func

# --- 7.3 Decorators ---
# A decorator is a function that takes another function and extends its behavior
# without explicitly modifying it.
def my_decorator(func):
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
  return wrapper

@my_decorator
def say_hello():
  print("Hello!")

say_hello()

# --- 7.4 Generators ---
# Generators are a simple way to create iterators. They use the 'yield' keyword.
# They "yield" one value at a time, which is memory efficient for large datasets.
def countdown(num):
  print("Starting countdown")
  while num > 0:
    yield num
    num -= 1

# Using the generator
cd = countdown(3)
print("First value:", next(cd))
print("Second value:", next(cd))
for value in cd:
    print("Remaining value:", value)


# ==============================================================================
# Part 8: The Python Standard Library
# ==============================================================================

print("\n--- Part 8: The Python Standard Library ---")
# Python has a "batteries-included" philosophy. Here are a few useful modules.

# 'os' - Interacting with the operating system
import os
print("Current working directory:", os.getcwd())

# 'random' - Generating random numbers
import random
print("Random integer between 1 and 10:", random.randint(1, 10))

# 'json' - Working with JSON data
import json
# A dictionary to convert to JSON
person_dict = {"name": "John", "age": 30, "city": "New York"}
# Convert Python dict to JSON string
json_string = json.dumps(person_dict)
print("JSON string:", json_string)
# Convert JSON string back to Python dict
parsed_dict = json.loads(json_string)
print("Parsed dictionary:", parsed_dict)


# ==============================================================================
# Part 9: Next Steps
# ==============================================================================

print("\n--- Part 9: Next Steps ---")

print("""
Congratulations on completing this whirlwind tour of Python!
You've covered a huge amount of ground, from the very basics to advanced concepts.

What's next?
1. Practice, Practice, Practice: The key to becoming a proficient programmer is to write code.
   Try solving problems on websites like LeetCode, HackerRank, or Codewars.

2. Build a Project: Apply what you've learned. Build a small project that interests you.
   - A simple calculator
   - A to-do list application
   - A web scraper for your favorite website

3. Explore Popular Libraries: The real power of Python for many developers comes from its
   vast ecosystem of third-party libraries. Based on your interests, you might explore:
   - Data Science/AI: NumPy, Pandas, Scikit-learn, Matplotlib, TensorFlow, PyTorch
   - Web Development: Flask, Django
   - Automation: Selenium, Beautiful Soup

4. Read the Official Documentation: The Python documentation (docs.python.org) is an
   excellent and authoritative resource.

Keep coding, stay curious, and have fun!
""")

print("\n--- End of Your Python Journey (for now!) ---")
