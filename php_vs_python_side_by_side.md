# PHP vs Python: Side-by-Side Code Comparison
## Complete Reference Guide for PHP Developers Learning Python

---

## Table of Contents

1. [Basic Syntax](#basic-syntax)
2. [Variables & Data Types](#variables--data-types)
3. [Strings](#strings)
4. [Arrays & Collections](#arrays--collections)
5. [Control Structures](#control-structures)
6. [Functions](#functions)
7. [Classes & Objects](#classes--objects)
8. [File Operations](#file-operations)
9. [Database Operations](#database-operations)
10. [Web Framework Comparison](#web-framework-comparison)
11. [API Development](#api-development)
12. [Common Patterns](#common-patterns)

---

## Basic Syntax

### Hello World

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
echo "Hello, World!";
print "Hello, World!";
?>
```

</td>
<td>

```python
print("Hello, World!")
# That's it! No tags needed
```

</td>
</tr>
</table>

### Comments

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Single line comment

# Also single line

/*
Multi-line comment
spanning multiple lines
*/

/**
 * DocBlock comment
 * @param string $name
 */
?>
```

</td>
<td>

```python
# Single line comment

"""
Multi-line comment
spanning multiple lines
(actually a docstring)
"""

'''
Can also use single quotes
for multi-line strings/comments
'''

def greet(name):
    """
    DocString for documentation
    Args:
        name (str): The name to greet
    """
    pass
```

</td>
</tr>
</table>

### Code Blocks

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Braces define blocks
if ($condition) {
    echo "True";
    echo "Still in block";
}

// One-liner without braces
if ($condition)
    echo "True";
?>
```

</td>
<td>

```python
# Indentation defines blocks
if condition:
    print("True")
    print("Still in block")

# Indentation is mandatory!
if condition:
    print("True")  # 4 spaces indent
```

</td>
</tr>
</table>

---

## Variables & Data Types

### Variable Declaration

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Variables start with $
$name = "John";
$age = 30;
$price = 19.99;
$is_active = true;
$nothing = null;

// No type declaration needed
$dynamic = "string";
$dynamic = 42;  // Now it's an int
?>
```

</td>
<td>

```python
# No $ prefix needed
name = "John"
age = 30
price = 19.99
is_active = True  # Capital T
nothing = None    # Capital N

# Dynamic typing
dynamic = "string"
dynamic = 42  # Now it's an int

# Type hints (optional)
name: str = "John"
age: int = 30
```

</td>
</tr>
</table>

### Type Checking

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$value = 42;

// Type checking
var_dump(gettype($value));  // "integer"
var_dump(is_int($value));   // true
var_dump(is_string($value)); // false
var_dump(is_array($value));  // false
var_dump(is_null($value));   // false

// Type conversion
$str = (string)$value;
$int = (int)"123";
$float = (float)"19.99";
$bool = (bool)$value;
?>
```

</td>
<td>

```python
value = 42

# Type checking
print(type(value))        # <class 'int'>
print(isinstance(value, int))     # True
print(isinstance(value, str))     # False
print(isinstance(value, list))    # False
print(value is None)              # False

# Type conversion
str_val = str(value)
int_val = int("123")
float_val = float("19.99")
bool_val = bool(value)
```

</td>
</tr>
</table>

### Constants

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Old style
define('API_KEY', 'abc123');
define('MAX_USERS', 100);

// Modern style (PHP 7.1+)
const API_KEY = 'abc123';
const MAX_USERS = 100;

echo API_KEY;
echo MAX_USERS;
?>
```

</td>
<td>

```python
# Convention: ALL_CAPS for constants
# (not enforced, just convention)
API_KEY = 'abc123'
MAX_USERS = 100

print(API_KEY)
print(MAX_USERS)

# In Python 3.8+, you can use Final
from typing import Final

API_KEY: Final = 'abc123'
MAX_USERS: Final[int] = 100
```

</td>
</tr>
</table>

---

## Strings

### String Operations

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$name = "John";
$age = 30;

// Concatenation
$greeting = "Hello " . $name;
$info = $name . " is " . $age;

// Interpolation (double quotes)
$greeting = "Hello $name";
$info = "$name is $age years old";
$info = "{$name} is {$age}";

// Single quotes (no interpolation)
$literal = 'Hello $name';  // Literal

// Multi-line
$multiline = "Line 1
Line 2
Line 3";

$heredoc = <<<EOT
Line 1
Line 2
Line 3
EOT;
?>
```

</td>
<td>

```python
name = "John"
age = 30

# Concatenation
greeting = "Hello " + name
info = name + " is " + str(age)

# f-strings (Python 3.6+) - BEST
greeting = f"Hello {name}"
info = f"{name} is {age} years old"

# .format() method
greeting = "Hello {}".format(name)
info = "{} is {}".format(name, age)

# % formatting (old style)
greeting = "Hello %s" % name
info = "%s is %d" % (name, age)

# Multi-line
multiline = """Line 1
Line 2
Line 3"""

# Or
multiline = ("Line 1\n"
             "Line 2\n"
             "Line 3")
```

</td>
</tr>
</table>

### String Methods

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$text = "Hello World";

// Length
strlen($text);              // 11

// Case conversion
strtoupper($text);          // "HELLO WORLD"
strtolower($text);          // "hello world"
ucfirst($text);             // "Hello world"
ucwords($text);             // "Hello World"

// Trim
trim(" hello ");            // "hello"
ltrim(" hello");            // "hello"
rtrim("hello ");            // "hello"

// Replace
str_replace("World", "PHP", $text);

// Split
explode(" ", $text);        // ["Hello", "World"]

// Join
implode(", ", ["a", "b"]);  // "a, b"

// Substring
substr($text, 0, 5);        // "Hello"

// Position
strpos($text, "World");     // 6
str_contains($text, "World"); // true (PHP 8+)

// Repeat
str_repeat("Ha", 3);        // "HaHaHa"
?>
```

</td>
<td>

```python
text = "Hello World"

# Length
len(text)                   # 11

# Case conversion
text.upper()                # "HELLO WORLD"
text.lower()                # "hello world"
text.capitalize()           # "Hello world"
text.title()                # "Hello World"

# Trim
" hello ".strip()           # "hello"
" hello".lstrip()           # "hello"
"hello ".rstrip()           # "hello"

# Replace
text.replace("World", "Python")

# Split
text.split(" ")             # ["Hello", "World"]

# Join
", ".join(["a", "b"])       # "a, b"

# Substring (slicing)
text[0:5]                   # "Hello"
text[:5]                    # "Hello"
text[6:]                    # "World"

# Position
text.find("World")          # 6
"World" in text             # True

# Repeat
"Ha" * 3                    # "HaHaHa"
```

</td>
</tr>
</table>

---

## Arrays & Collections

### Indexed Arrays / Lists

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Creating arrays
$fruits = array("apple", "banana", "orange");
$fruits = ["apple", "banana", "orange"];  // Short syntax

// Accessing elements
echo $fruits[0];            // "apple"
echo $fruits[1];            // "banana"

// Adding elements
$fruits[] = "grape";        // Append
array_push($fruits, "mango");
array_unshift($fruits, "kiwi"); // Prepend

// Removing elements
array_pop($fruits);         // Remove last
array_shift($fruits);       // Remove first
unset($fruits[1]);          // Remove by index

// Array length
count($fruits);

// Check if exists
in_array("apple", $fruits);
isset($fruits[0]);

// Slicing
array_slice($fruits, 0, 2);

// Merging
$combined = array_merge($arr1, $arr2);

// Sorting
sort($fruits);              // Ascending
rsort($fruits);             // Descending

// Iteration
foreach ($fruits as $fruit) {
    echo $fruit;
}

foreach ($fruits as $index => $fruit) {
    echo "$index: $fruit";
}
?>
```

</td>
<td>

```python
# Creating lists
fruits = ["apple", "banana", "orange"]

# Accessing elements
print(fruits[0])            # "apple"
print(fruits[1])            # "banana"
print(fruits[-1])           # "orange" (last)

# Adding elements
fruits.append("grape")      # Append
fruits.insert(0, "kiwi")    # Insert at position
fruits.extend(["mango", "peach"])  # Add multiple

# Removing elements
fruits.pop()                # Remove last
fruits.pop(0)               # Remove by index
fruits.remove("apple")      # Remove by value
del fruits[1]               # Remove by index

# List length
len(fruits)

# Check if exists
"apple" in fruits
0 < len(fruits)             # Check index exists

# Slicing
fruits[0:2]                 # First 2
fruits[:2]                  # First 2
fruits[1:]                  # All but first
fruits[-2:]                 # Last 2

# Merging
combined = arr1 + arr2

# Sorting
fruits.sort()               # In-place ascending
fruits.sort(reverse=True)   # In-place descending
sorted(fruits)              # Returns new sorted list

# Iteration
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

</td>
</tr>
</table>

### Associative Arrays / Dictionaries

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Creating associative arrays
$person = array(
    "name" => "John",
    "age" => 30,
    "email" => "john@example.com"
);

// Short syntax
$person = [
    "name" => "John",
    "age" => 30,
    "email" => "john@example.com"
];

// Accessing values
echo $person["name"];       // "John"
echo $person["age"];        // 30

// Adding/updating
$person["city"] = "New York";
$person["age"] = 31;

// Removing
unset($person["email"]);

// Check if key exists
isset($person["name"]);
array_key_exists("name", $person);

// Get all keys
array_keys($person);

// Get all values
array_values($person);

// Iteration
foreach ($person as $key => $value) {
    echo "$key: $value";
}

// Only keys
foreach (array_keys($person) as $key) {
    echo $key;
}

// Only values
foreach ($person as $value) {
    echo $value;
}

// Count
count($person);

// Merge
$merged = array_merge($arr1, $arr2);
?>
```

</td>
<td>

```python
# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Accessing values
print(person["name"])       # "John"
print(person["age"])        # 30
print(person.get("age"))    # 30
print(person.get("phone", "N/A"))  # Default

# Adding/updating
person["city"] = "New York"
person["age"] = 31

# Removing
del person["email"]
person.pop("email")         # Remove and return
person.pop("phone", None)   # With default

# Check if key exists
"name" in person
person.get("name") is not None

# Get all keys
person.keys()               # dict_keys object
list(person.keys())         # As list

# Get all values
person.values()             # dict_values object
list(person.values())       # As list

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")

# Only keys
for key in person:
    print(key)

for key in person.keys():
    print(key)

# Only values
for value in person.values():
    print(value)

# Count
len(person)

# Merge (Python 3.9+)
merged = arr1 | arr2
# Or
merged = {**arr1, **arr2}
# Or
merged = arr1.copy()
merged.update(arr2)
```

</td>
</tr>
</table>

### List Comprehensions vs Array Functions

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$numbers = [1, 2, 3, 4, 5];

// Map - transform each element
$squared = array_map(function($x) {
    return $x * $x;
}, $numbers);
// [1, 4, 9, 16, 25]

// Filter - keep elements matching condition
$evens = array_filter($numbers, function($x) {
    return $x % 2 == 0;
});
// [2, 4]

// Reduce - combine to single value
$sum = array_reduce($numbers, function($carry, $x) {
    return $carry + $x;
}, 0);
// 15

// Chaining operations
$result = array_map(function($x) {
    return $x * 2;
}, array_filter($numbers, function($x) {
    return $x > 2;
}));
// [6, 8, 10]
?>
```

</td>
<td>

```python
numbers = [1, 2, 3, 4, 5]

# List comprehension - transform
squared = [x * x for x in numbers]
# [1, 4, 9, 16, 25]

# List comprehension - filter
evens = [x for x in numbers if x % 2 == 0]
# [2, 4]

# Reduce
from functools import reduce
sum_val = reduce(lambda carry, x: carry + x, numbers, 0)
# 15

# Or just use built-in
sum_val = sum(numbers)

# Map (returns iterator)
squared = list(map(lambda x: x * x, numbers))

# Filter (returns iterator)
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Chaining with comprehension
result = [x * 2 for x in numbers if x > 2]
# [6, 8, 10]

# Complex comprehension
result = [
    x * 2 
    for x in numbers 
    if x > 2 
    if x < 5
]
# [6, 8]
```

</td>
</tr>
</table>

---

## Control Structures

### If Statements

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$age = 25;

// Basic if
if ($age >= 18) {
    echo "Adult";
}

// If-else
if ($age >= 18) {
    echo "Adult";
} else {
    echo "Minor";
}

// If-elseif-else
if ($age >= 65) {
    echo "Senior";
} elseif ($age >= 18) {
    echo "Adult";
} elseif ($age >= 13) {
    echo "Teen";
} else {
    echo "Child";
}

// Ternary operator
$status = ($age >= 18) ? "adult" : "minor";

// Null coalescing (PHP 7+)
$name = $userName ?? "Guest";

// Null coalescing assignment (PHP 7.4+)
$name ??= "Guest";
?>
```

</td>
<td>

```python
age = 25

# Basic if
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"

# Get with default
name = user_name if user_name else "Guest"

# Or using walrus operator (Python 3.8+)
if (name := get_user_name()) is not None:
    print(f"Hello {name}")
```

</td>
</tr>
</table>

### Switch / Match Statements

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
$day = "Monday";

// Switch statement
switch ($day) {
    case "Monday":
    case "Tuesday":
    case "Wednesday":
    case "Thursday":
    case "Friday":
        echo "Weekday";
        break;
    case "Saturday":
    case "Sunday":
        echo "Weekend";
        break;
    default:
        echo "Invalid day";
}

// Switch with return (PHP 8+)
$result = match ($day) {
    "Monday", "Tuesday", 
    "Wednesday", "Thursday", 
    "Friday" => "Weekday",
    "Saturday", "Sunday" => "Weekend",
    default => "Invalid day"
};
?>
```

</td>
<td>

```python
day = "Monday"

# Traditional if-elif (before Python 3.10)
if day in ["Monday", "Tuesday", "Wednesday", 
           "Thursday", "Friday"]:
    result = "Weekday"
elif day in ["Saturday", "Sunday"]:
    result = "Weekend"
else:
    result = "Invalid day"

# Match statement (Python 3.10+)
match day:
    case "Monday" | "Tuesday" | "Wednesday" | \
         "Thursday" | "Friday":
        result = "Weekday"
    case "Saturday" | "Sunday":
        result = "Weekend"
    case _:
        result = "Invalid day"

# Dictionary mapping (common pattern)
day_type = {
    "Monday": "Weekday",
    "Tuesday": "Weekday",
    "Wednesday": "Weekday",
    "Thursday": "Weekday",
    "Friday": "Weekday",
    "Saturday": "Weekend",
    "Sunday": "Weekend"
}
result = day_type.get(day, "Invalid day")
```

</td>
</tr>
</table>

### Loops

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// For loop
for ($i = 0; $i < 10; $i++) {
    echo $i;
}

// While loop
$count = 0;
while ($count < 10) {
    echo $count;
    $count++;
}

// Do-while loop
$count = 0;
do {
    echo $count;
    $count++;
} while ($count < 10);

// Foreach loop
$fruits = ["apple", "banana", "orange"];
foreach ($fruits as $fruit) {
    echo $fruit;
}

// Foreach with index
foreach ($fruits as $index => $fruit) {
    echo "$index: $fruit";
}

// Break and continue
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) {
        break;  // Exit loop
    }
    if ($i == 3) {
        continue;  // Skip iteration
    }
    echo $i;
}
?>
```

</td>
<td>

```python
# For loop with range
for i in range(10):
    print(i)

# For loop with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# While loop
count = 0
while count < 10:
    print(count)
    count += 1

# No do-while in Python
# Use while True with break
count = 0
while True:
    print(count)
    count += 1
    if count >= 10:
        break

# For loop over list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# For loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Break and continue
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i == 3:
        continue  # Skip iteration
    print(i)

# For-else (unique to Python!)
for i in range(10):
    if i == 15:
        break
else:
    print("Loop completed without break")
```

</td>
</tr>
</table>

---

## Functions

### Basic Functions

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Basic function
function greet($name) {
    return "Hello, " . $name;
}

echo greet("John");

// Default parameters
function greet($name = "Guest") {
    return "Hello, " . $name;
}

// Type declarations (PHP 7+)
function add(int $a, int $b): int {
    return $a + $b;
}

// Multiple return values (using array)
function getCoordinates() {
    return [10, 20];
}
list($x, $y) = getCoordinates();

// Or using array destructuring (PHP 7.1+)
[$x, $y] = getCoordinates();

// Variable number of arguments
function sum(...$numbers) {
    return array_sum($numbers);
}
echo sum(1, 2, 3, 4);  // 10

// Named arguments (PHP 8+)
function createUser($name, $email, $age = 0) {
    // ...
}
createUser(
    name: "John",
    age: 30,
    email: "john@example.com"
);
?>
```

</td>
<td>

```python
# Basic function
def greet(name):
    return f"Hello, {name}"

print(greet("John"))

# Default parameters
def greet(name="Guest"):
    return f"Hello, {name}"

# Type hints (Python 3.5+)
def add(a: int, b: int) -> int:
    return a + b

# Multiple return values (tuple)
def get_coordinates():
    return 10, 20

x, y = get_coordinates()

# Or explicitly as tuple
def get_coordinates():
    return (10, 20)

# Variable number of arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4))  # 10

# Keyword arguments
def create_user(name, email, age=0):
    pass

# Positional
create_user("John", "john@example.com", 30)

# Keyword
create_user(
    name="John",
    age=30,
    email="john@example.com"
)
```

</td>
</tr>
</table>

### Advanced Function Features

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Anonymous function (closure)
$greet = function($name) {
    return "Hello, " . $name;
};
echo $greet("John");

// Arrow function (PHP 7.4+)
$square = fn($x) => $x * $x;
echo $square(5);  // 25

// Closure with use
$multiplier = 2;
$multiply = function($x) use ($multiplier) {
    return $x * $multiplier;
};
echo $multiply(5);  // 10

// Higher-order functions
function applyOperation($numbers, $operation) {
    return array_map($operation, $numbers);
}

$squared = applyOperation([1, 2, 3], fn($x) => $x * $x);

// Callable type
function executeCallback(callable $callback) {
    return $callback();
}
?>
```

</td>
<td>

```python
# Lambda (anonymous function)
greet = lambda name: f"Hello, {name}"
print(greet("John"))

# Lambda with single expression
square = lambda x: x * x
print(square(5))  # 25

# Closure
multiplier = 2
def multiply(x):
    return x * multiplier

print(multiply(5))  # 10

# Or with lambda
multiply = lambda x: x * multiplier

# Higher-order functions
def apply_operation(numbers, operation):
    return list(map(operation, numbers))

squared = apply_operation([1, 2, 3], lambda x: x * x)

# Function as parameter
def execute_callback(callback):
    return callback()

# Decorators (function modifying functions)
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    return f"Hello, {name}"
```

</td>
</tr>
</table>

### *args and **kwargs

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Variable arguments
function sum(...$numbers) {
    return array_sum($numbers);
}
echo sum(1, 2, 3);  // 6

// Unpacking array as arguments
$numbers = [1, 2, 3];
sum(...$numbers);  // 6

// Named parameters (PHP 8+)
function createUser(
    string $name,
    string $email,
    int $age = 0,
    ...$options
) {
    print_r($options);
}

createUser(
    "John",
    "john@example.com",
    role: "admin",
    active: true
);
?>
```

</td>
<td>

```python
# *args - variable positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6

# **kwargs - variable keyword arguments
def create_user(name, email, **kwargs):
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Options: {kwargs}")

create_user(
    "John",
    "john@example.com",
    role="admin",
    active=True
)

# Combining both
def flexible_function(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function(1, 2, 3, name="John", age=30)

# Unpacking
numbers = [1, 2, 3]
sum_all(*numbers)  # Unpack list

options = {"role": "admin", "active": True}
create_user("John", "john@example.com", **options)
```

</td>
</tr>
</table>

---

## Classes & Objects

### Basic Class Definition

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
class User {
    // Properties
    public $name;
    public $email;
    private $password;
    protected $role;
    
    // Static property
    public static $count = 0;
    
    // Constructor
    public function __construct($name, $email) {
        $this->name = $name;
        $this->email = $email;
        self::$count++;
    }
    
    // Method
    public function greet() {
        return "Hello, I'm " . $this->name;
    }
    
    // Static method
    public static function getCount() {
        return self::$count;
    }
    
    // Magic method
    public function __toString() {
        return $this->name;
    }
}

// Creating instance
$user = new User("John", "john@example.com");
echo $user->greet();
echo $user->name;

// Static access
echo User::$count;
echo User::getCount();
?>
```

</td>
<td>

```python
class User:
    # Class variable (like static)
    count = 0
    
    # Constructor
    def __init__(self, name, email):
        # Instance variables (like properties)
        self.name = name
        self.email = email
        self._password = None  # Convention: _ = protected
        self.__secret = None   # __ = private (name mangling)
        User.count += 1
    
    # Instance method
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    # Class method (like static)
    @classmethod
    def get_count(cls):
        return cls.count
    
    # Static method
    @staticmethod
    def validate_email(email):
        return "@" in email
    
    # Magic method
    def __str__(self):
        return self.name

# Creating instance (no 'new' keyword)
user = User("John", "john@example.com")
print(user.greet())
print(user.name)

# Class variable access
print(User.count)
print(User.get_count())
print(User.validate_email("test@example.com"))
```

</td>
</tr>
</table>

### Properties and Getters/Setters

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
class User {
    private $firstName;
    private $lastName;
    
    public function __construct($firstName, $lastName) {
        $this->firstName = $firstName;
        $this->lastName = $lastName;
    }
    
    // Getter
    public function getFullName() {
        return $this->firstName . ' ' . $this->lastName;
    }
    
    // Setter
    public function setFullName($fullName) {
        [$this->firstName, $this->lastName] = 
            explode(' ', $fullName, 2);
    }
    
    // Magic getters/setters
    public function __get($property) {
        return $this->$property ?? null;
    }
    
    public function __set($property, $value) {
        $this->$property = $value;
    }
}

$user = new User("John", "Doe");
echo $user->getFullName();  // "John Doe"
$user->setFullName("Jane Smith");
?>
```

</td>
<td>

```python
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    # Property decorator (like getter)
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    # Setter
    @full_name.setter
    def full_name(self, value):
        self._first_name, self._last_name = \
            value.split(' ', 1)
    
    # Deleter (optional)
    @full_name.deleter
    def full_name(self):
        self._first_name = None
        self._last_name = None

# Usage - looks like attribute access
user = User("John", "Doe")
print(user.full_name)  # "John Doe" (calls getter)
user.full_name = "Jane Smith"  # Calls setter
del user.full_name  # Calls deleter
```

</td>
</tr>
</table>

### Inheritance

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Parent class
class User {
    protected $name;
    protected $email;
    
    public function __construct($name, $email) {
        $this->name = $name;
        $this->email = $email;
    }
    
    public function greet() {
        return "Hello, I'm " . $this->name;
    }
}

// Child class
class Admin extends User {
    private $permissions;
    
    public function __construct($name, $email, $permissions) {
        parent::__construct($name, $email);
        $this->permissions = $permissions;
    }
    
    // Override method
    public function greet() {
        return "Hello, I'm Admin " . $this->name;
    }
    
    // Call parent method
    public function parentGreet() {
        return parent::greet();
    }
}

$admin = new Admin("John", "john@example.com", ["all"]);
echo $admin->greet();  // "Hello, I'm Admin John"
?>
```

</td>
<td>

```python
# Parent class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def greet(self):
        return f"Hello, I'm {self.name}"

# Child class
class Admin(User):
    def __init__(self, name, email, permissions):
        # Call parent constructor
        super().__init__(name, email)
        self.permissions = permissions
    
    # Override method
    def greet(self):
        return f"Hello, I'm Admin {self.name}"
    
    # Call parent method
    def parent_greet(self):
        return super().greet()

# Multiple inheritance (Python supports it)
class Loggable:
    def log(self, message):
        print(f"[LOG] {message}")

class SuperAdmin(Admin, Loggable):
    pass

admin = Admin("John", "john@example.com", ["all"])
print(admin.greet())  # "Hello, I'm Admin John"
```

</td>
</tr>
</table>

### Abstract Classes and Interfaces

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Interface
interface Loggable {
    public function log($message);
}

// Abstract class
abstract class Animal {
    protected $name;
    
    abstract public function makeSound();
    
    public function getName() {
        return $this->name;
    }
}

// Implementing interface and extending abstract
class Dog extends Animal implements Loggable {
    public function __construct($name) {
        $this->name = $name;
    }
    
    public function makeSound() {
        return "Woof!";
    }
    
    public function log($message) {
        echo "[DOG LOG] $message";
    }
}

$dog = new Dog("Buddy");
echo $dog->makeSound();
$dog->log("Dog created");
?>
```

</td>
<td>

```python
from abc import ABC, abstractmethod

# Abstract base class (like interface + abstract)
class Loggable(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def get_name(self):
        return self.name

# Implementing abstract classes (multiple inheritance)
class Dog(Animal, Loggable):
    def make_sound(self):
        return "Woof!"
    
    def log(self, message):
        print(f"[DOG LOG] {message}")

dog = Dog("Buddy")
print(dog.make_sound())
dog.log("Dog created")

# Protocol (Python 3.8+) - like structural interface
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...
```

</td>
</tr>
</table>

---

## File Operations

### Reading and Writing Files

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Read entire file
$content = file_get_contents('file.txt');

// Read file line by line
$lines = file('file.txt');
foreach ($lines as $line) {
    echo $line;
}

// Read with file handle
$handle = fopen('file.txt', 'r');
while (($line = fgets($handle)) !== false) {
    echo $line;
}
fclose($handle);

// Write to file (overwrite)
file_put_contents('file.txt', "Hello World");

// Append to file
file_put_contents('file.txt', "New line", FILE_APPEND);

// Write with file handle
$handle = fopen('file.txt', 'w');
fwrite($handle, "Hello World\n");
fwrite($handle, "Line 2\n");
fclose($handle);

// Check if file exists
if (file_exists('file.txt')) {
    echo "File exists";
}

// Delete file
unlink('file.txt');

// Get file size
filesize('file.txt');

// Get file info
$info = pathinfo('path/to/file.txt');
echo $info['dirname'];    // 'path/to'
echo $info['basename'];   // 'file.txt'
echo $info['filename'];   // 'file'
echo $info['extension'];  // 'txt'
?>
```

</td>
<td>

```python
# Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Read file line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()

# Write to file (overwrite)
with open('file.txt', 'w') as f:
    f.write("Hello World\n")

# Append to file
with open('file.txt', 'a') as f:
    f.write("New line\n")

# Write multiple lines
with open('file.txt', 'w') as f:
    f.write("Hello World\n")
    f.write("Line 2\n")
    # Or
    f.writelines(['Line 1\n', 'Line 2\n'])

# Check if file exists
import os
if os.path.exists('file.txt'):
    print("File exists")

# Delete file
os.remove('file.txt')

# Get file size
os.path.getsize('file.txt')

# Get file info
import pathlib
path = pathlib.Path('path/to/file.txt')
print(path.parent)       # 'path/to'
print(path.name)         # 'file.txt'
print(path.stem)         # 'file'
print(path.suffix)       # '.txt'
```

</td>
</tr>
</table>

### JSON Operations

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Array/object to JSON
$data = [
    "name" => "John",
    "age" => 30,
    "hobbies" => ["reading", "coding"]
];

$json = json_encode($data);
echo $json;
// {"name":"John","age":30,"hobbies":["reading","coding"]}

// Pretty print
$json = json_encode($data, JSON_PRETTY_PRINT);

// JSON to array
$decoded = json_decode($json, true);

// JSON to object
$obj = json_decode($json);
echo $obj->name;

// Read JSON file
$data = json_decode(file_get_contents('data.json'), true);

// Write JSON file
file_put_contents('data.json', json_encode($data));

// Error handling
$json = json_encode($data);
if (json_last_error() !== JSON_ERROR_NONE) {
    echo "JSON Error: " . json_last_error_msg();
}
?>
```

</td>
<td>

```python
import json

# Dictionary to JSON
data = {
    "name": "John",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

json_str = json.dumps(data)
print(json_str)
# {"name": "John", "age": 30, "hobbies": ["reading", "coding"]}

# Pretty print
json_str = json.dumps(data, indent=2)

# JSON to dictionary
decoded = json.loads(json_str)

# Read JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Error handling
try:
    data = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")

# Custom encoder for datetime
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps(data, cls=DateTimeEncoder)
```

</td>
</tr>
</table>

### CSV Operations

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Read CSV
$file = fopen('users.csv', 'r');
while (($row = fgetcsv($file)) !== false) {
    print_r($row);
}
fclose($file);

// Read with headers
$file = fopen('users.csv', 'r');
$headers = fgetcsv($file);
while (($row = fgetcsv($file)) !== false) {
    $data = array_combine($headers, $row);
    echo $data['name'];
}
fclose($file);

// Write CSV
$file = fopen('output.csv', 'w');
fputcsv($file, ['Name', 'Email', 'Age']);
fputcsv($file, ['John', 'john@example.com', 30]);
fputcsv($file, ['Jane', 'jane@example.com', 25]);
fclose($file);

// Read entire CSV to array
$data = array_map('str_getcsv', file('users.csv'));
?>
```

</td>
<td>

```python
import csv

# Read CSV
with open('users.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Read with headers (DictReader)
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'])

# Write CSV
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email', 'Age'])
    writer.writerow(['John', 'john@example.com', 30])
    writer.writerow(['Jane', 'jane@example.com', 25])

# Write with headers (DictWriter)
with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'email', 'age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'John', 
                     'email': 'john@example.com', 
                     'age': 30})

# Read entire CSV to list
with open('users.csv', 'r') as f:
    data = list(csv.reader(f))
```

</td>
</tr>
</table>

---

## Database Operations

### Database Connection

<table>
<tr>
<th>PHP (PDO)</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// PostgreSQL with PDO
try {
    $pdo = new PDO(
        'pgsql:host=localhost;dbname=mydb',
        'user',
        'password'
    );
    $pdo->setAttribute(
        PDO::ATTR_ERRMODE,
        PDO::ERRMODE_EXCEPTION
    );
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// MySQL with PDO
$pdo = new PDO(
    'mysql:host=localhost;dbname=mydb;charset=utf8mb4',
    'user',
    'password'
);

// SQLite with PDO
$pdo = new PDO('sqlite:database.db');
?>
```

</td>
<td>

```python
# PostgreSQL with psycopg2
import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="user",
        password="password"
    )
except psycopg2.Error as e:
    print(f"Connection failed: {e}")

# MySQL with mysql.connector
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="mydb",
    user="user",
    password="password"
)

# SQLite with sqlite3
import sqlite3

conn = sqlite3.connect('database.db')
```

</td>
</tr>
</table>

### CRUD Operations

<table>
<tr>
<th>PHP (PDO)</th>
<th>Python (psycopg2)</th>
</tr>
<tr>
<td>

```php
<?php
// SELECT
$stmt = $pdo->prepare(
    'SELECT * FROM users WHERE age > :age'
);
$stmt->execute(['age' => 18]);
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);

foreach ($users as $user) {
    echo $user['name'];
}

// SELECT single row
$stmt = $pdo->prepare(
    'SELECT * FROM users WHERE id = :id'
);
$stmt->execute(['id' => 1]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

// INSERT
$stmt = $pdo->prepare(
    'INSERT INTO users (name, email, age) 
     VALUES (:name, :email, :age)'
);
$stmt->execute([
    'name' => 'John',
    'email' => 'john@example.com',
    'age' => 30
]);
$lastId = $pdo->lastInsertId();

// UPDATE
$stmt = $pdo->prepare(
    'UPDATE users SET age = :age WHERE id = :id'
);
$stmt->execute(['age' => 31, 'id' => 1]);
$rowCount = $stmt->rowCount();

// DELETE
$stmt = $pdo->prepare(
    'DELETE FROM users WHERE id = :id'
);
$stmt->execute(['id' => 1]);

// Transaction
try {
    $pdo->beginTransaction();
    
    $pdo->exec("INSERT INTO users ...");
    $pdo->exec("UPDATE accounts ...");
    
    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
    throw $e;
}
?>
```

</td>
<td>

```python
# SELECT
cursor = conn.cursor()
cursor.execute(
    'SELECT * FROM users WHERE age > %s',
    (18,)
)
users = cursor.fetchall()

for user in users:
    print(user[0])  # Or use column name

# SELECT with DictCursor
import psycopg2.extras
cursor = conn.cursor(
    cursor_factory=psycopg2.extras.DictCursor
)
cursor.execute('SELECT * FROM users')
for user in cursor.fetchall():
    print(user['name'])

# SELECT single row
cursor.execute(
    'SELECT * FROM users WHERE id = %s',
    (1,)
)
user = cursor.fetchone()

# INSERT
cursor.execute(
    'INSERT INTO users (name, email, age) '
    'VALUES (%s, %s, %s) RETURNING id',
    ('John', 'john@example.com', 30)
)
last_id = cursor.fetchone()[0]
conn.commit()

# UPDATE
cursor.execute(
    'UPDATE users SET age = %s WHERE id = %s',
    (31, 1)
)
row_count = cursor.rowcount
conn.commit()

# DELETE
cursor.execute(
    'DELETE FROM users WHERE id = %s',
    (1,)
)
conn.commit()

# Transaction
try:
    cursor.execute("INSERT INTO users ...")
    cursor.execute("UPDATE accounts ...")
    conn.commit()
except Exception as e:
    conn.rollback()
    raise e
finally:
    cursor.close()
    conn.close()
```

</td>
</tr>
</table>

### Context Managers for Database

<table>
<tr>
<th>PHP</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// No built-in context manager
// Manual cleanup needed
try {
    $pdo = new PDO(...);
    $stmt = $pdo->prepare(...);
    $stmt->execute(...);
    $results = $stmt->fetchAll();
} finally {
    $pdo = null;  // Close connection
}

// Or using a wrapper
class Database {
    private $pdo;
    
    public function __construct() {
        $this->pdo = new PDO(...);
    }
    
    public function __destruct() {
        $this->pdo = null;
    }
}
?>
```

</td>
<td>

```python
# Using context manager (with statement)
with psycopg2.connect(...) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
# Connection automatically closed

# Or
from contextlib import closing

with closing(psycopg2.connect(...)) as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def get_db_cursor():
    conn = psycopg2.connect(...)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

# Usage
with get_db_cursor() as cursor:
    cursor.execute('SELECT * FROM users')
```

</td>
</tr>
</table>

---

## Web Framework Comparison

### Routing

<table>
<tr>
<th>PHP (Laravel)</th>
<th>Python (Django)</th>
</tr>
<tr>
<td>

```php
<?php
// routes/web.php

use App\Http\Controllers\UserController;

// Basic route
Route::get('/', function () {
    return view('welcome');
});

// Controller route
Route::get('/users', [UserController::class, 'index']);
Route::get('/users/{id}', [UserController::class, 'show']);
Route::post('/users', [UserController::class, 'store']);
Route::put('/users/{id}', [UserController::class, 'update']);
Route::delete('/users/{id}', [UserController::class, 'destroy']);

// Resource route (all CRUD routes)
Route::resource('users', UserController::class);

// Route groups
Route::prefix('api')->group(function () {
    Route::get('/users', [UserController::class, 'index']);
});

// Named routes
Route::get('/profile', function () {
    //
})->name('profile');

// Route with middleware
Route::get('/admin', function () {
    //
})->middleware('auth');
?>
```

</td>
<td>

```python
# urls.py
from django.urls import path, include
from . import views

# Basic URLconf
urlpatterns = [
    # Function-based views
    path('', views.index, name='index'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    
    # Class-based views
    path('users/', views.UserListView.as_view()),
    
    # Include other URL configs
    path('api/', include('api.urls')),
]

# Using ViewSets (like resource routes)
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

# URL patterns with regex
from django.urls import re_path

urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]

# Named URLs (reverse lookup)
from django.urls import reverse
url = reverse('user-detail', kwargs={'pk': 1})
```

</td>
</tr>
</table>

### Views/Controllers

<table>
<tr>
<th>PHP (Laravel)</th>
<th>Python (Django)</th>
</tr>
<tr>
<td>

```php
<?php
namespace App\Http\Controllers;

use App\Models\User;
use Illuminate\Http\Request;

class UserController extends Controller
{
    // List all users
    public function index()
    {
        $users = User::all();
        return view('users.index', ['users' => $users]);
    }
    
    // Show single user
    public function show($id)
    {
        $user = User::findOrFail($id);
        return view('users.show', ['user' => $user]);
    }
    
    // Create user form
    public function create()
    {
        return view('users.create');
    }
    
    // Store new user
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|max:255',
            'email' => 'required|email|unique:users',
        ]);
        
        $user = User::create($validated);
        
        return redirect()->route('users.show', $user->id);
    }
    
    // Update user
    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);
        $user->update($request->all());
        
        return redirect()->route('users.show', $user->id);
    }
    
    // Delete user
    public function destroy($id)
    {
        User::destroy($id);
        return redirect()->route('users.index');
    }
    
    // JSON response
    public function apiIndex()
    {
        $users = User::all();
        return response()->json($users);
    }
}
?>
```

</td>
<td>

```python
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import User
from .forms import UserForm

# Function-based views
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'users/create.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user-list')

# JSON response
def api_user_list(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

# Class-based views
from django.views.generic import ListView, DetailView

class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'
```

</td>
</tr>
</table>

### Models/ORM

<table>
<tr>
<th>PHP (Laravel Eloquent)</th>
<th>Python (Django ORM)</th>
</tr>
<tr>
<td>

```php
<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    // Table name (auto-detected if not set)
    protected $table = 'users';
    
    // Primary key
    protected $primaryKey = 'id';
    
    // Fillable fields
    protected $fillable = [
        'name',
        'email',
        'age',
    ];
    
    // Hidden fields (for JSON)
    protected $hidden = [
        'password',
    ];
    
    // Casts
    protected $casts = [
        'is_active' => 'boolean',
        'created_at' => 'datetime',
    ];
    
    // Relationships
    public function posts()
    {
        return $this->hasMany(Post::class);
    }
    
    public function roles()
    {
        return $this->belongsToMany(Role::class);
    }
    
    // Scopes
    public function scopeActive($query)
    {
        return $query->where('is_active', true);
    }
    
    // Accessors
    public function getFullNameAttribute()
    {
        return $this->first_name . ' ' . $this->last_name;
    }
    
    // Mutators
    public function setEmailAttribute($value)
    {
        $this->attributes['email'] = strtolower($value);
    }
}

// Usage
$users = User::all();
$user = User::find(1);
$users = User::where('age', '>', 18)->get();
$user = User::create(['name' => 'John', 'email' => 'john@example.com']);
?>
```

</td>
<td>

```python
# models.py
from django.db import models

class User(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    # Properties (like accessors)
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    # Custom save (like mutators)
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
    
    # Relationships
    # In Post model:
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Many-to-many
    # roles = models.ManyToManyField(Role)

# Custom manager (like scopes)
class UserManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

class User(models.Model):
    # ... fields ...
    objects = UserManager()

# Usage
users = User.objects.all()
user = User.objects.get(pk=1)
users = User.objects.filter(age__gt=18)
user = User.objects.create(name='John', email='john@example.com')
users = User.objects.active()  # Custom manager
```

</td>
</tr>
</table>

---

## API Development

### REST API with JSON Response

<table>
<tr>
<th>PHP (Laravel)</th>
<th>Python (Django REST Framework)</th>
</tr>
<tr>
<td>

```php
<?php
namespace App\Http\Controllers\Api;

use App\Models\User;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;
use App\Http\Resources\UserResource;

class UserController extends Controller
{
    // GET /api/users
    public function index()
    {
        $users = User::all();
        return UserResource::collection($users);
    }
    
    // GET /api/users/{id}
    public function show($id)
    {
        $user = User::findOrFail($id);
        return new UserResource($user);
    }
    
    // POST /api/users
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users',
            'age' => 'nullable|integer|min:0',
        ]);
        
        $user = User::create($validated);
        
        return new UserResource($user);
    }
    
    // PUT /api/users/{id}
    public function update(Request $request, $id)
    {
        $user = User::findOrFail($id);
        
        $validated = $request->validate([
            'name' => 'sometimes|string|max:255',
            'email' => 'sometimes|email|unique:users,email,'.$id,
            'age' => 'nullable|integer|min:0',
        ]);
        
        $user->update($validated);
        
        return new UserResource($user);
    }
    
    // DELETE /api/users/{id}
    public function destroy($id)
    {
        User::destroy($id);
        return response()->json(null, 204);
    }
}

// Resource (Transformer)
namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class UserResource extends JsonResource
{
    public function toArray($request)
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'age' => $this->age,
            'created_at' => $this->created_at->toDateTimeString(),
        ];
    }
}
?>
```

</td>
<td>

```python
# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_email(self, value):
        if 'test' in value:
            raise serializers.ValidationError('Test emails not allowed')
        return value.lower()

# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# ViewSet (handles all CRUD operations)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Or function-based views
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
```

</td>
</tr>
</table>

---

## Common Patterns

### Dependency Injection

<table>
<tr>
<th>PHP (Laravel)</th>
<th>Python</th>
</tr>
<tr>
<td>

```php
<?php
// Service
class UserService
{
    protected $repository;
    
    public function __construct(UserRepository $repository)
    {
        $this->repository = $repository;
    }
    
    public function createUser($data)
    {
        return $this->repository->create($data);
    }
}

// Controller with DI
class UserController extends Controller
{
    protected $userService;
    
    public function __construct(UserService $userService)
    {
        $this->userService = $userService;
    }
    
    public function store(Request $request)
    {
        $user = $this->userService->createUser($request->all());
        return response()->json($user);
    }
}

// Service Provider
class AppServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->app->bind(UserRepository::class, function () {
            return new UserRepository();
        });
    }
}
?>
```

</td>
<td>

```python
# Python doesn't have built-in DI container
# But you can use patterns or libraries

# Simple DI pattern
class UserRepository:
    def create(self, data):
        # Create user
        pass

class UserService:
    def __init__(self, repository=None):
        self.repository = repository or UserRepository()
    
    def create_user(self, data):
        return self.repository.create(data)

# Using dependency-injector library
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    user_repository = providers.Singleton(UserRepository)
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )

# Usage
container = Container()
user_service = container.user_service()

# Or manual injection
class UserView:
    def __init__(self, user_service):
        self.user_service = user_service
    
    def post(self, request):
        user = self.user_service.create_user(request.data)
        return JsonResponse({'user': user})
```

</td>
</tr>
</table>

### Environment Configuration

<table>
<tr>
<th>PHP (Laravel)</th>
<th>Python (Django)</th>
</tr>
<tr>
<td>

```php
<?php
// .env file
APP_NAME=MyApp
APP_ENV=production
APP_DEBUG=false
DB_HOST=localhost
DB_DATABASE=mydb
DB_USERNAME=user
DB_PASSWORD=secret

// config/database.php
return [
    'connections' => [
        'mysql' => [
            'host' => env('DB_HOST', 'localhost'),
            'database' => env('DB_DATABASE'),
            'username' => env('DB_USERNAME'),
            'password' => env('DB_PASSWORD'),
        ],
    ],
];

// Usage
$host = config('database.connections.mysql.host');
$debug = env('APP_DEBUG', false);
?>
```

</td>
<td>

```python
# .env file
APP_NAME=MyApp
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost/mydb

# settings.py
import os
from decouple import config, Csv

# Basic
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Or using dj-database-url
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# List from env
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
```

</td>
</tr>
</table>

---

## Summary: Key Differences

| Feature | PHP | Python |
|---------|-----|--------|
| **Syntax** | C-like with `{}` | Indentation-based |
| **Variables** | `$variable` | `variable` |
| **Arrays** | Single `array` type | Lists, tuples, dicts, sets |
| **Strings** | `.` for concatenation | `+` or f-strings |
| **Booleans** | `true`/`false` | `True`/`False` |
| **Null** | `null` | `None` |
| **Functions** | `function name() {}` | `def name():` |
| **Classes** | `new Class()` | `Class()` |
| **This** | `$this` | `self` |
| **Static** | `self::` or `static::` | `cls` or direct access |
| **Imports** | `require`/`use` | `import`/`from` |
| **Error Handling** | `try/catch` | `try/except` |
| **Iteration** | `foreach` | `for ... in` |
| **List Ops** | Array functions | List comprehensions |
| **Framework** | Laravel/Symfony | Django/Flask |
| **ORM** | Eloquent/Doctrine | Django ORM/SQLAlchemy |
| **Package Manager** | Composer | pip |
| **Virtual Env** | Not standard | venv/virtualenv |

---

**This guide provides side-by-side comparisons to help PHP developers quickly understand Python equivalents and patterns. Happy coding! 🐍**
