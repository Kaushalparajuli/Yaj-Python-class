# Python Crash Course for PHP Developers
## Transitioning to Python & Django

**Duration:** 5 Days (Intensive)  
**Target Audience:** PHP Developers  
**Goal:** Quickly ramp up on Python fundamentals and prepare for Django development

---

## Course Overview

This crash course is designed specifically for developers with PHP experience who need to quickly transition to Python and Django. We'll leverage your existing programming knowledge while highlighting key differences and Python-specific patterns.

---

## Day 1: Python Fundamentals & Syntax Comparison

### Session 1: Environment Setup & Python Basics (2 hours)

**Topics:**
- Installing Python (3.11+) and pip
- Virtual environments (venv) - Python's equivalent to Composer
- Python REPL and interactive development
- Running Python scripts

**PHP vs Python Comparisons:**
- `<?php ?>` tags → No tags needed in Python
- `$variable` → `variable` (no $ prefix)
- `echo` / `print` → `print()`
- `;` semicolons → Not required (newline-based)
- `{}` blocks → Indentation-based blocks

**Hands-on:**
```python
# Hello World
print("Hello, Python!")

# Variables (no $ prefix!)
name = "John"
age = 30

# Comments
# Single line comment
"""
Multi-line comment
or docstring
"""
```

### Session 2: Data Types & Variables (2 hours)

**Topics:**
- Basic data types: int, float, str, bool
- Type hints (optional but recommended)
- String operations and f-strings
- None vs PHP's null
- Dynamic typing

**PHP → Python Equivalents:**
```python
# PHP: $name = "John";
name = "John"

# PHP: $count = 42;
count = 42

# PHP: $price = 19.99;
price = 19.99

# PHP: $is_active = true;
is_active = True  # Note: Capital T

# PHP: $value = null;
value = None  # Note: Capital N

# String interpolation
# PHP: "Hello $name"
# Python:
greeting = f"Hello {name}"  # f-strings (Python 3.6+)

# Type hints (optional)
def greet(name: str):
    return f"Hello {name}"
```

**Hands-on:**
- Variable declarations and type checking
- String formatting exercises
- Type conversion practices

### Session 3: Collections & Data Structures (2 hours)

**Topics:**
- Lists (like PHP arrays)
	•	Mutable (you can change items)
	•	Ordered
	•	Can store mixed data types
- Tuples (immutable lists)
	•	Immutable: cannot modify after creation
	•	Ordered
	•	Used for fixed data
- Dictionaries (like PHP associative arrays)
	•	Key-value pairs
	•	Keys must be unique
	•	Similar to PHP associative arrays
- Sets
	•	Unordered collection
	•	No duplicate values
	•	Useful for uniqueness checks
- List comprehensions
	•	A concise way to create lists
	•	Replaces loops for generating new lists

**PHP → Python Equivalents:**
```python
# PHP: $fruits = array("apple", "banana");
# Python List:
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits[0])  # apple

# PHP: $person = array("name" => "John", "age" => 30);
# Python Dictionary:
person = {"name": "John", "age": 30}
print(person["name"])  # John
person["email"] = "john@example.com"

# PHP: foreach ($fruits as $fruit)
# Python:
for fruit in fruits:
    print(fruit)

# PHP: foreach ($person as $key => $value)
# Python:
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehension (powerful Python feature!)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary comprehension
person_upper = {k: v.upper() if isinstance(v, str) else v 
                for k, v in person.items()}
```

**Hands-on:**
- Converting PHP arrays to Python lists/dicts
- List manipulation exercises
- Dictionary operations

### Session 4: Control Flow (2 hours)

**Topics:**
- if/elif/else statements
- Comparison operators
- Logical operators (and, or, not)
- Truthiness in Python
- Ternary operators

**PHP → Python Equivalents:**
```python
# PHP: if ($age >= 18) { }
# Python:
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

# PHP: $status = ($age >= 18) ? "adult" : "minor";
# Python ternary:
status = "adult" if age >= 18 else "minor"

# PHP: if ($name && $age)
# Python:
if name and age:
    print("Both exist")

# PHP: if (!$is_active)
# Python:
if not is_active:
    print("Inactive")

# Truthiness
# False: None, False, 0, "", [], {}, ()
# True: Everything else
if user_list:  # Checks if list is not empty
    print("Has users")
```

---

## Day 2: Functions, Loops & Error Handling

### Session 1: Functions (2 hours)

**Topics:**
- Function definition and calling
- Parameters: positional, keyword, default values
- *args and **kwargs
- Return values
- Lambda functions
- Decorators (intro)

**PHP → Python Equivalents:**
```python
# PHP: function greet($name) { return "Hello $name"; }
# Python:
def greet(name):
    return f"Hello {name}"

# Default parameters
# PHP: function greet($name = "Guest")
def greet(name="Guest"):
    return f"Hello {name}"

# Type hints
def greet(name: str, age: int = 0) -> str:
    return f"Hello {name}, age {age}"

# Variable arguments
# PHP: function sum(...$numbers)
def sum_all(*numbers):
    return sum(numbers)

# Keyword arguments
def create_user(name, email, **options):
    user = {"name": name, "email": email}
    user.update(options)
    return user

# Lambda (anonymous function)
# PHP: $square = fn($x) => $x * $x;
square = lambda x: x * x

# Higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### Session 2: Loops & Iterations (2 hours)

**Topics:**
- for loops
- while loops
- break, continue, pass
- enumerate() and zip()
- range() function
- Iterators and generators (intro)

**PHP → Python Equivalents:**
```python
# PHP: for ($i = 0; $i < 10; $i++)
# Python:
for i in range(10):
    print(i)

# PHP: foreach ($items as $item)
for item in items:
    print(item)

# PHP: foreach ($items as $index => $item)
for index, item in enumerate(items):
    print(f"{index}: {item}")

# PHP: while ($count < 10)
count = 0
while count < 10:
    print(count)
    count += 1

# Zip two lists
names = ["John", "Jane", "Bob"]
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Loop with else (unique to Python!)
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed without break")
```

### Session 3: Exception Handling (2 hours)

**Topics:**
- try/except blocks
- Multiple exception types
- finally clause
- Raising exceptions
- Custom exceptions
- Context managers (with statement)

**PHP → Python Equivalents:**
```python
# PHP: try { } catch (Exception $e) { } finally { }
# Python:
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"General error: {e}")
finally:
    print("Cleanup")

# Raising exceptions
# PHP: throw new Exception("Error");
# Python:
raise ValueError("Invalid value")

# Custom exceptions
class InvalidUserError(Exception):
    pass

# Context managers (auto cleanup)
# PHP: $file = fopen(); ... fclose($file);
# Python:
with open('file.txt', 'r') as file:
    content = file.read()
# File automatically closed


### Session 4: File Operations (1.5 hours)

**Topics:**
- Reading and writing files
- File modes
- Working with paths
- JSON operations
- CSV operations

```python
# Reading files
with open('data.txt', 'r') as f:
    content = f.read()
    
# Writing files
with open('output.txt', 'w') as f:
    f.write("Hello World\n")

# Reading lines
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())

# JSON
import json

# PHP: json_encode()
data = {"name": "John", "age": 30}
json_string = json.dumps(data)

# PHP: json_decode()
parsed = json.loads(json_string)

# File operations
import json
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# CSV
import csv
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['email'])
```

---

## Day 3: Object-Oriented Programming

### Session 1: Classes & Objects (2 hours)

**Topics:**
- Class definition
- __init__ constructor
- Instance vs class variables
- Methods
- self parameter
- Property decorators

**PHP → Python Equivalents:**
```python
# PHP: class User { public $name; }
# Python:
class User:
    # self = “this object”.
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    def __str__(self):
        # PHP: __toString()
        return f"User({self.name})"

# Creating instance
# PHP: $user = new User("John");
user = User("John", "john@example.com")
print(user.greet())

# Class variables
class User:
    # PHP: public static $count = 0;
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        User.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Properties
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property # getter
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @full_name.setter # setter
    def full_name(self, value):
        self._first_name, self._last_name = value.split(' ', 1)

user = User("John", "Doe")
print(user.full_name)  # John Doe
user.full_name = "Jane Smith"
```

# Properties PHP equievalent
```php
class User {
    private $first_name;
    private $last_name;

    public function __construct($first, $last) {
        $this->first_name = $first;
        $this->last_name = $last;
    }

    public function getFullName() {
        return $this->first_name . " " . $this->last_name;
    }

    public function setFullName($value) {
        [$this->first_name, $this->last_name] = explode(" ", $value, 2);
    }
}
```

### Session 2: Inheritance & Polymorphism (2 hours)

**Topics:**
- Class inheritance
- Method overriding
- super() function
- Multiple inheritance
- Abstract classes
- Magic methods

```python
# Basic inheritance
# PHP: class Admin extends User
class Admin(User):
    def __init__(self, name, email, permissions):
        super().__init__(name, email)
        self.permissions = permissions
    
    def greet(self):
        return f"Hello, I'm Admin {self.name}"

# Multiple inheritance
class Loggable:
    def log(self, message):
        print(f"[LOG] {message}")

class AdminUser(User, Loggable):
    pass

admin = AdminUser("John", "john@example.com")
admin.log("User created")

# Abstract classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Magic methods
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: ${self.price}"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
```

### Session 3: Modules & Packages (2 hours)

**Topics:**
- Importing modules
- Creating modules
- Package structure
- __init__.py files
- Relative vs absolute imports
- Common standard library modules

```python
# PHP: require 'file.php'; include 'file.php';
# Python imports:

# Import entire module
import math
print(math.sqrt(16))

# Import specific items
from math import sqrt, pi
print(sqrt(16))

# Import with alias
import datetime as dt
now = dt.datetime.now()

# Import everything (not recommended)
from math import *

# Creating a module
# File: mymodule.py
def greet(name):
    return f"Hello {name}"

PI = 3.14159

# Using it:
import mymodule
print(mymodule.greet("John"))

# Package structure
"""
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
"""

# Importing from package
from mypackage import module1
from mypackage.subpackage import module3

# Common standard library modules
import os           # Operating system
import sys          # System-specific
import datetime     # Date and time
import json         # JSON operations
import re           # Regular expressions
import random       # Random numbers
import pathlib      # Path operations
from collections import defaultdict, Counter
from functools import wraps
```

### Session 4: Python Tooling (1.5 hours)

**Topics:**
- pip and package management
- requirements.txt
- Virtual environments in depth
- Code formatting (black, autopep8)
- Linting (pylint, flake8)
- Type checking (mypy)

```bash
# Creating virtual environment
python -m venv venv

# Activating
# Linux/Mac: source venv/bin/activate
# Windows: venv\Scripts\activate

# Installing packages
pip install django requests psycopg2-binary

# Saving dependencies
pip freeze > requirements.txt

# Installing from requirements
pip install -r requirements.txt

# Common development packages
pip install black pylint mypy pytest

# Using black for formatting
black myfile.py

# Type checking
mypy myfile.py
```

---

## Day 4: Python for Web Development

### Session 1: Working with Databases (2 hours)

**Topics:**
- Database connections
- psycopg2 for PostgreSQL
- sqlite3 module
- Basic SQL operations
- Connection pooling
- Context managers for DB

```python
# SQLite example
import sqlite3

# PHP: $conn = new PDO('sqlite:database.db');
# Python:
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

# Insert
# PHP: $stmt->execute([':name' => $name]);
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
               ('John', 'john@example.com'))
conn.commit()

# Query
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)

conn.close()

# PostgreSQL with psycopg2
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="user",
    password="password"
)

# Using context manager
with conn.cursor() as cursor:
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
```

### Session 2: HTTP & APIs (2 hours)

**Topics:**
- requests library
- Making HTTP calls
- REST API consumption
- JSON handling
- Authentication
- Error handling in requests

```python
import requests

# PHP: file_get_contents() or cURL
# Python requests:

# GET request
response = requests.get('https://api.example.com/users')
print(response.status_code)
print(response.json())

# POST request
data = {'name': 'John', 'email': 'john@example.com'}
response = requests.post('https://api.example.com/users', json=data)

# Headers and authentication
headers = {
    'Authorization': 'Bearer token123',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.example.com/profile', headers=headers)

# Query parameters
params = {'page': 1, 'limit': 10}
response = requests.get('https://api.example.com/users', params=params)

# Error handling
try:
    response = requests.get('https://api.example.com/users', timeout=5)
    response.raise_for_status()  # Raises exception for 4xx/5xx
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# Session for multiple requests
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token123'})
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')
```

### Session 3: Async Python Basics (2 hours)

**Topics:**
- async/await syntax
- asyncio basics
- Async vs sync
- When to use async
- Basic async patterns

```python
import asyncio
import aiohttp

# Async function
async def fetch_user(user_id):
    await asyncio.sleep(1)  # Simulating I/O
    return {"id": user_id, "name": f"User {user_id}"}

# Running async code
async def main():
    user = await fetch_user(1)
    print(user)

# Run it
asyncio.run(main())

# Multiple concurrent tasks
async def fetch_multiple_users():
    tasks = [fetch_user(i) for i in range(1, 6)]
    users = await asyncio.gather(*tasks)
    return users

# Async HTTP requests
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_multiple_apis():
    urls = [
        'https://api.example.com/users/1',
        'https://api.example.com/users/2',
        'https://api.example.com/users/3'
    ]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
```

### Session 4: Testing in Python (1.5 hours)

**Topics:**
- unittest module
- pytest framework
- Test structure
- Fixtures
- Mocking
- Test coverage

```python
# Using pytest (recommended)
# test_user.py

def test_user_creation():
    user = User("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"

def test_user_greet():
    user = User("John", "john@example.com")
    assert user.greet() == "Hello, I'm John"

# Fixtures
import pytest

@pytest.fixture
def sample_user():
    return User("John", "john@example.com")

def test_with_fixture(sample_user):
    assert sample_user.name == "John"

# Mocking
from unittest.mock import Mock, patch

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'id': 1}
        result = fetch_user_data(1)
        assert result['id'] == 1

# Running tests
# pytest test_user.py
# pytest --cov=myapp tests/
```

---

## Day 5: Django Introduction & PHP to Django Migration

### Session 1: Django Fundamentals (2 hours)

**Topics:**
- Django project structure
- MVT pattern (Model-View-Template)
- Settings configuration
- URL routing
- Views and responses
- Django vs Laravel/Symfony comparison

```python
# Creating a Django project
django-admin startproject myproject
cd myproject
python manage.py startapp users

# Project structure
"""
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py    # Like config/app.php in Laravel
        urls.py        # Like routes/web.php
        wsgi.py
        asgi.py
    users/
        __init__.py
        models.py      # Like Eloquent models
        views.py       # Like Controllers
        urls.py
        admin.py
        tests.py
"""

# settings.py configuration
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'users',  # Your app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# URL routing
# myproject/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('<int:user_id>/', views.user_detail, name='user-detail'),
]

# Views
# users/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import User

# Function-based view (like PHP controllers)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})

# Class-based view
from django.views import View

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/list.html', {'users': users})
    
    def post(self, request):
        # Handle user creation
        pass
```

### Session 2: Django Models (ORM) (2 hours)

**Topics:**
- Model definition
- Field types
- Relationships
- QuerySet API
- Migrations
- Django ORM vs PHP ORMs (Eloquent, Doctrine)

```python
# models.py
from django.db import models
from django.contrib.auth.models import User as AuthUser

# PHP Eloquent: class User extends Model
# Django:
class User(models.Model):
    # Fields
    name = models.CharField(max_length=100)
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

# Relationships
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

# Migrations
# python manage.py makemigrations
# python manage.py migrate

# QuerySet API (like Eloquent)

# PHP: User::all()
users = User.objects.all()

# PHP: User::find($id)
user = User.objects.get(id=1)

# PHP: User::where('age', '>', 18)->get()
users = User.objects.filter(age__gt=18)

# PHP: User::where('name', 'like', '%john%')->get()
users = User.objects.filter(name__icontains='john')

# PHP: User::orderBy('created_at', 'desc')->limit(10)
users = User.objects.order_by('-created_at')[:10]

# Relationships
# PHP: $user->posts
posts = user.posts.all()

# PHP: Post::with('author')->get()
posts = Post.objects.select_related('author').all()

# PHP: Post::with('tags')->get()
posts = Post.objects.prefetch_related('tags').all()

# Aggregation
from django.db.models import Count, Avg

# Count posts per user
User.objects.annotate(post_count=Count('posts'))

# Average age
User.objects.aggregate(avg_age=Avg('age'))

# Creating records
user = User.objects.create(name='John', email='john@example.com')

# Or
user = User(name='John', email='john@example.com')
user.save()

# Updating
User.objects.filter(id=1).update(name='Jane')

# Deleting
User.objects.filter(id=1).delete()
```

### Session 3: Django Forms & Templates (2 hours)

**Topics:**
- Django template language
- Template inheritance
- Forms and validation
- CSRF protection
- Static files
- Django templates vs Blade/Twig

```python
# Forms
# forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

# Using forms in views
from django.shortcuts import render, redirect

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user-detail', user_id=user.id)
    else:
        form = UserForm()
    
    return render(request, 'users/create.html', {'form': form})

# Templates
# templates/base.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
"""

# templates/users/list.html
"""
{% extends 'base.html' %}

{% block title %}Users{% endblock %}

{% block content %}
    <h1>Users</h1>
    
    {% if users %}
        <ul>
        {% for user in users %}
            <li>
                {{ user.name }} - {{ user.email }}
                {% if user.is_active %}
                    <span>Active</span>
                {% endif %}
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No users found.</p>
    {% endif %}
{% endblock %}
"""

# Template filters
"""
{{ user.name|upper }}
{{ user.created_at|date:"Y-m-d" }}
{{ user.bio|truncatewords:50 }}
{{ user.email|default:"No email" }}
"""
```

### Session 4: Django REST Framework & Migration Tips (2 hours)

**Topics:**
- Django REST Framework basics
- Serializers
- API views
- Authentication
- Migration strategies from PHP to Django
- Best practices

```python
# Install: pip install djangorestframework

# Serializers (like PHP transformers)
# serializers.py
from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'created_at', 'post_count']
        read_only_fields = ['id', 'created_at']
    
    def validate_email(self, value):
        if 'test' in value:
            raise serializers.ValidationError('Test emails not allowed')
        return value

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'

# API Views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

# Class-based API views
from rest_framework import generics

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets (like PHP Resource Controllers)
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# URLs for ViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

# Authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
```

---

## PHP to Python Quick Reference

### Syntax Comparison Cheat Sheet

| PHP | Python | Notes |
|-----|--------|-------|
| `$variable` | `variable` | No $ prefix |
| `define('CONST', 'value')` | `CONST = 'value'` | Module-level constants |
| `echo`, `print` | `print()` | Function call required |
| `array()`, `[]` | `[]` | Lists |
| `[]` (assoc array) | `{}` | Dictionaries |
| `null` | `None` | Capitalized |
| `true`, `false` | `True`, `False` | Capitalized |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` | Words, not symbols |
| `.` (concat) | `+` or f-strings | String concatenation |
| `->` | `.` | Object member access |
| `::` | `.` | Class member access |
| `function name()` | `def name():` | Indentation-based |
| `class Name {}` | `class Name:` | Indentation-based |
| `new Class()` | `Class()` | No 'new' keyword |
| `$this` | `self` | In class methods |
| `__construct` | `__init__` | Constructor |
| `extends` | `(ParentClass)` | Inheritance |
| `interface` | `ABC` | Abstract base class |
| `namespace` | module/package | File-based modules |
| `use`, `require` | `import` | Module imports |
| `try/catch` | `try/except` | Exception handling |
| `foreach` | `for ... in` | Iteration |
| `count()` | `len()` | Get length |
| `is_array()` | `isinstance(x, list)` | Type checking |
| `json_encode()` | `json.dumps()` | JSON serialization |
| `json_decode()` | `json.loads()` | JSON parsing |
| `$_GET`, `$_POST` | `request.GET`, `request.POST` | Django |
| `$_SESSION` | `request.session` | Django |

---

## Migration Checklist: PHP to Django

### 1. **Environment Setup**
- [ ] Install Python 3.11+
- [ ] Set up virtual environment
- [ ] Install Django and dependencies
- [ ] Configure database connections
- [ ] Set up version control

### 2. **Database Migration**
- [ ] Export existing database schema
- [ ] Create Django models matching schema
- [ ] Generate migrations
- [ ] Migrate data (use Django management commands)
- [ ] Verify data integrity

### 3. **Code Migration Strategy**
- [ ] Map PHP routes to Django URLs
- [ ] Convert controllers to Django views
- [ ] Convert models to Django ORM models
- [ ] Migrate business logic to Python
- [ ] Convert templates (Blade/Twig → Django templates)

### 4. **Authentication & Authorization**
- [ ] Set up Django authentication
- [ ] Migrate user accounts
- [ ] Implement permission system
- [ ] Set up session management
- [ ] Configure CSRF protection

### 5. **API Development**
- [ ] Install Django REST Framework
- [ ] Create serializers
- [ ] Implement API endpoints
- [ ] Set up authentication (Token/JWT)
- [ ] Document APIs

### 6. **Testing**
- [ ] Write unit tests
- [ ] Write integration tests
- [ ] Test API endpoints
- [ ] Performance testing
- [ ] Security testing

### 7. **Deployment**
- [ ] Set up production server (Gunicorn/uWSGI)
- [ ] Configure web server (Nginx/Apache)
- [ ] Set up static file serving
- [ ] Configure logging
- [ ] Set up monitoring

---

## Common Pitfalls & Tips

### 1. **Indentation Matters!**
```python
# Wrong - will cause IndentationError
def my_function():
print("Hello")

# Correct
def my_function():
    print("Hello")
```

### 2. **Mutable Default Arguments**
```python
# Wrong - dangerous!
def append_to(item, list=[]):
    list.append(item)
    return list

# Correct
def append_to(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list
```

### 3. **String Concatenation**
```python
# Not Pythonic
name = "John"
greeting = "Hello " + name + "!"

# Pythonic - use f-strings
greeting = f"Hello {name}!"
```

### 4. **List Comprehensions**
```python
# Instead of loops
squares = []
for x in range(10):
    squares.append(x**2)

# Use list comprehension
squares = [x**2 for x in range(10)]
```

### 5. **Django QuerySet Evaluation**
```python
# Lazy evaluation - no DB hit yet
users = User.objects.filter(age__gt=18)

# Now it hits the database
for user in users:
    print(user.name)
```

---

## Practice Projects

### Day 1-2: Python Basics
- **Todo List CLI**: Command-line todo app with file storage
- **Data Parser**: Parse CSV/JSON files and generate reports
- **Contact Manager**: Store and search contacts

### Day 3: OOP
- **Library Management System**: Books, members, borrowing system
- **Bank Account Simulator**: Accounts, transactions, inheritance

### Day 4: Web/APIs
- **Weather App**: Fetch weather data from API
- **URL Shortener**: Simple URL shortening service
- **API Consumer**: Consume and display data from public APIs

### Day 5: Django
- **Blog API**: Full CRUD blog with Django REST Framework
- **User Management System**: Authentication, profiles, admin panel
- **Task Manager**: Team collaboration tool

---

## Resources

### Official Documentation
- Python: https://docs.python.org/3/
- Django: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/

### Learning Resources
- Real Python: https://realpython.com/
- Django for Beginners: https://djangoforbeginners.com/
- Python Package Index (PyPI): https://pypi.org/

### Tools
- VS Code with Python extension
- PyCharm (IDE)
- Postman (API testing)
- Django Debug Toolbar

### Community
- r/Python
- r/django
- Django Discord
- Stack Overflow

---

## Assessment & Next Steps

### Knowledge Check
- [ ] Can write Python functions and classes
- [ ] Understand Python data structures
- [ ] Comfortable with Django models
- [ ] Can create REST APIs
- [ ] Understand Django ORM queries
- [ ] Can deploy Django applications

### After This Course
1. **Practice**: Build real projects
2. **Advanced Django**: Celery, Redis, WebSockets
3. **Testing**: Pytest, Django testing best practices
4. **Deployment**: Docker, AWS, DigitalOcean
5. **Advanced Python**: Decorators, metaclasses, async programming

---

## Daily Schedule Template

**9:00 AM - 11:00 AM**: Theory & Examples  
**11:00 AM - 11:15 AM**: Break  
**11:15 AM - 1:00 PM**: Hands-on Practice  
**1:00 PM - 2:00 PM**: Lunch  
**2:00 PM - 4:00 PM**: Advanced Topics & Project Work  
**4:00 PM - 4:15 PM**: Break  
**4:15 PM - 5:30 PM**: Q&A, Code Review, Exercises  

---

## Course Completion Certificate

Upon completion, developers should be able to:
- Write idiomatic Python code
- Build REST APIs with Django
- Understand Django ORM and database operations
- Deploy Django applications
- Migrate PHP applications to Python/Django

---

**Good luck with your Python/Django journey! 🐍🚀**
