# 1. What is the expected output of the following python code given below-

data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter (lambda x: x>4, data)
print(list(result))  # output [10, 501, 22, 37, 100, 999, 87, 351]

# 2. Write a python code using lambda function to check every element of a list is an integer or a string ?

# Define a list with mixed types
mixed_list = ['automation', 'hello', 20, 'world', 30, 'guvi', 35, 'zen']

# Lambda function to check if an element is an integer or a string
check_type = lambda x: isinstance(x, int) or isinstance(x, str)

# Used map function to apply the lambda function to each element in the list
result = all(map(check_type, mixed_list))

# Print the result
if result:
    print("All elements are integers or strings.")
else:
    print("Not all elements are integers or strings.")

# 3. Using python lambda function create a Fibbnacci series from 1 to 50 elements?
    
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Generate Fibonacci series up to 50 elements

fib_series = [fibonacci(i) for i in range(50)]

print(fib_series)

# 4. Write a python function to validate the regular expression of following -
# a. Email address
# b. Mobile numbers of Bangladesh
# c. Telephone numbers of USA
# d. 16 characters alpha-numeric password composed of alphabets of upper case, lower case, special characters, numbers?

import re

def validate_email(email):
    # Regular expression for validating email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_bangladeshi_mobile_number(number):
    # Regular expression for validating Bangladeshi mobile numbers
    pattern = r'^\+?(?:88)?01[3-9]\d{8}$'
    return re.match(pattern, number) is not None

def validate_usa_telephone_number(number):
    # Regular expression for validating USA telephone numbers
    pattern = r'^\+?1\s*(?:\(\d{3}\)|\d{3})[-\s]?\d{3}[-\s]?\d{4}$'
    return re.match(pattern, number) is not None

def validate_password(password):
    # Regular expression for validating 16 characters alpha-numeric password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    return re.match(pattern, password) is not None

# Test the functions

email = "example@example.com"
mobile_number = "+8801712345678"
telephone_number = "+1 (123) 456-7890"
password = "Password@1234"

print("Email validation result:", validate_email(email))
print("Bangladeshi mobile number validation result:", validate_bangladeshi_mobile_number(mobile_number))
print("USA telephone number validation result:", validate_usa_telephone_number(telephone_number))
print("Password validation result:", validate_password(password))

