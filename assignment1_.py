# Part 1: Data Types and Variables

# Q1: Create variables of different types and print their type
# Integer
num_var = 100  # Example of an integer
print(f"Integer: {num_var}, Type: {type(num_var)}")

# Float
price = 9.99  # Example of a float
print(f"Float: {price}, Type: {type(price)}")

# String
message = "Welcome to Python Programming!"  # Example of a string
print(f"String: {message}, Type: {type(message)}")

# Boolean
is_active = False  # Example of a boolean
print(f"Boolean: {is_active}, Type: {type(is_active)}")

# Q2: Combine first and last names into a full name and print the length
# Take user input for first and last name
given_name = input("Enter your first name: ")
surname = input("Enter your last name: ")

# Combine first and last name
complete_name = given_name + " " + surname
print(f"Full Name: {complete_name}")

# Print the length of the full name
print(f"Length of Full Name: {len(complete_name)}")

# Q3: Currency Converter
# Store the exchange rate from USD to Euros
usd_to_eur_rate = 0.92  # Updated rate, 1 USD = 0.92 Euros

# Take user input for the amount in USD
dollar_amount = float(input("Enter the amount in USD: "))

# Convert to Euros
euro_amount = dollar_amount * usd_to_eur_rate
print(f"Equivalent Amount in Euros: {euro_amount:.2f}")

# Part 2: Operators

# Q4: Perform arithmetic operations
input_number = float(input("Enter a number: "))

# Square of the number
squared_value = input_number ** 2
print(f"Square of {input_number}: {squared_value}")

# Cube of the number
cubed_value = input_number ** 3
print(f"Cube of {input_number}: {cubed_value}")

# Square root of the number
sqrt_value = input_number ** 0.5
print(f"Square root of {input_number}: {sqrt_value}")

# Q5: Comparison and logical operators
# Take a number as input
check_num = int(input("Enter a number: "))

# Check if the number is positive and even
if check_num > 0 and check_num % 2 == 0:
    print(f"{check_num} is positive and even.")

# Check if the number is greater than 10 or less than -10
if check_num > 10 or check_num < -10:
    print(f"{check_num} is greater than 10 or less than -10.")

# Check if the number is neither positive nor divisible by 5
if not (check_num > 0 or check_num % 5 == 0):
    print(f"{check_num} is neither positive nor divisible by 5.")

# Part 3: Functions

# Q6: Function to calculate rectangle area
def rectangle_area(length, width):
    """Calculates the area of a rectangle."""
    return length * width

# Test the function
rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))
print(f"Area of the rectangle: {rectangle_area(rect_length, rect_width)}")

# Q7: Temperature converter from Fahrenheit to Celsius
def temperature_converter(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

# Test the function
fahren_temp = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {temperature_converter(fahren_temp):.2f}")

# Q8: Function to calculate simple interest
def simple_interest(principal, rate, time):
    """Calculates simple interest."""
    return (principal * rate * time) / 100

# Test the function
principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter rate of interest: "))
time_period = float(input("Enter time in years: "))
print(f"Simple Interest: {simple_interest(principal_amount, interest_rate, time_period):.2f}")

# Q9: Fibonacci sequence
# Print the first 10 numbers in the Fibonacci sequence
fib_a, fib_b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(fib_a, end=" ")
    fib_a, fib_b = fib_b, fib_a + fib_b
print()

# Q10: Multiplication table using a while loop
table_number = int(input("Enter a number to print its multiplication table: "))
count = 1
while count <= 10:
    print(f"{table_number} x {count} = {table_number * count}")
    count += 1

# Q11: Iterate through a list and print even numbers
# Example list of integers
sample_numbers = [12, 15, 22, 33, 40, 51, 66, 78, 89, 90]
print("Even numbers in the list:")
for value in sample_numbers:
    if value % 2 == 0:
        print(value)
