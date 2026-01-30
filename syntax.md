# Comments
```python
"""
Multi-line comment
"""
```

# Variables
```python
name = "John"
age = 30
price = 99.99

# Type hints (optional)
name: str = "John"
age: int = 30
```

# Print Output
```python
print("Hello, World!")
print(name, age)
print(f"My name is {name}")
```

# Control Structures

### If Statements
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### Match
```python
match status:
    case "active":
        print("User is active")
    case "inactive":
        print("User is inactive")
    case _:  # default
        print("Unknown status")
```

# Loop Structures

### For Loops
```python
# (0 to 4)
for i in range(5):
    print(i)

# (1 to 5)
for i in range(1, 6):
    print(i)

# 0, 2, 4, 6, 8
for i in range(0, 10, 2):  
    print(i)

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# With index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

while count < 10:
    print(count)
    count += 1
else:
    print("Loop completed")
```

### Loop Control
```python
for i in range(10):
    if i == 3:
        continue 
    if i == 7:
        break 
    print(i)
```

# Data Types

### Lists
```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])  # "apple"
print(fruits[-1])  # "orange" (negative indexing)

# Add items
fruits.append("grape")
fruits.insert(1, "mango")

# Remove items
fruits.remove("banana")
last = fruits.pop()

# Length
print(len(fruits))

# Slice
print(fruits[1:3])  # Elements at index 1 and 2
```

### Dictionaries
```python
# Key-value pairs
user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

print(user["name"])
print(user.get("age"))  # safer (returns None if not found)

user["city"] = "New York"

# Loop through
for key, value in user.items():
    print(f"{key}: {value}")

# Keys only
for key in user.keys():
    print(key)

# Values only
for value in user.values():
```

### Tuples (immutable lists)
```python
# Cannot be changed after creation
coordinates = (10, 20)
rgb = (255, 128, 0)

# Unpacking
x, y = coordinates
r, g, b = rgb
```

### Sets (unique values)
```python
numbers = {1, 2, 3, 4, 4, 5}  # Duplicates removed
print(numbers)  # {1, 2, 3, 4, 5}

# Operations
numbers.add(6)
numbers.remove(2)
```

# Functions

### Basic Function
```python
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
print(greet("Bob", "Hi"))  # "Hi, Bob!"
```

### Multiple Return Values
```python
def get_user():
    return "John", 30, "john@example.com"

name, age, email = get_user()
```

### *args and **kwargs
```python
# Variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# Variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30)
```

### Lambda Functions (anonymous)
```python
square = lambda x: x ** 2
print(square(5))  # 25

# Often used with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
```

# String Operations    

### Common Methods
```python
text = "Hello, World!"

# Case
print(text.lower())  # "hello, world!"
print(text.upper())  # "HELLO, WORLD!"
print(text.title())  # "Hello, World!"

# Search
print(text.startswith("Hello"))  # True
print(text.endswith("!"))  # True
print(text.find("World"))  # 7 (index)

# Replace
print(text.replace("World", "Python"))

# Split
words = text.split(", ")  # ["Hello", "World!"]

# Join
result = "-".join(["a", "b", "c"])  # "a-b-c"

# Strip whitespace
text = "  hello  "
print(text.strip())  # "hello"
```

### String Formatting
```python
name = "Alice"
age = 30

# f-strings
print(f"Name: {name}, Age: {age}")

# format method
print("Name: {}, Age: {}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Old style
print("Name: %s, Age: %d" % (name, age))
```

# Classes (OOP)

### Basic Class
```python
class User:
    def __init__(self, name, age):  # Constructor
        self.name = name 
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def is_adult(self):
        return self.age >= 18

# Create instance
user = User("John", 30)
print(user.greet())
print(user.is_adult())
```

### Inheritance
```python
class Admin(User):
    def __init__(self, name, age, role):
        super().__init__(name, age)  # Call parent constructor
        self.role = role
    
    def greet(self):  # Override method
        return f"Hello, I'm {self.name}, a {self.role}"

admin = Admin("Alice", 35, "Super Admin")
print(admin.greet())
```

# File Operations

### Reading Files
```python
# Method 1: with statement (auto-closes file)
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Another line\n")

# Append
with open("output.txt", "a") as file:
    file.write("Appended line\n")
```


# Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always executes")

# Raise exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

# List Comprehensions

```python
# Create lists in one line
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = [x ** 2 for x in numbers]  # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in numbers if x % 2 == 0]  # [2, 4]

# Dictionary comprehension
squared_dict = {x: x**2 for x in numbers}  # {1: 1, 2: 4, 3: 9, ...}
```

# Useful Built-in Functions

```python
# Type checking
print(type(42))  # <class 'int'>
print(isinstance(42, int))  # True

# Conversion
int("42")  # String to int
str(42)  # Int to string
float("3.14")  # String to float

# Math
abs(-5)  # 5
round(3.7)  # 4
pow(2, 3)  # 8
max(1, 5, 3)  # 5
min(1, 5, 3)  # 1

# Lists
len([1, 2, 3])  # 3
sum([1, 2, 3])  # 6
sorted([3, 1, 2])  # [1, 2, 3]
reversed([1, 2, 3])  # iterator

# Others
range(5)  # 0, 1, 2, 3, 4
enumerate(['a', 'b'])  # (0, 'a'), (1, 'b')
zip([1, 2], ['a', 'b'])  # (1, 'a'), (2, 'b')
```