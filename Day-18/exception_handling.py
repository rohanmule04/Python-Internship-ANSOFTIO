# exception.py

try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    # Display result
    print("Division:", result)

# Handling division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Handling invalid input
except ValueError:
    print("Error: Please enter valid numbers")

# Handling any other unexpected error
except Exception as e:
    print("Unexpected error:", e)

# Optional (always runs)
finally:
    print("Program executed successfully")