
x = 1
y = 2
z = x + y
print('The sum of x and y is:', z)
"""
Hello
multiple lines of comments
"""
def greet(name):
    print('Hello, ' + name + '!')
    
greet('Alice')
greet('Bob')

try:
    result = 10 / 0
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print('An unexpected error occurred:', str(e))
finally:
    print('Execution completed.')
    