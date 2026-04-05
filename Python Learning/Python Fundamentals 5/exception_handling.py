# Exception Handling in Python
# ===========================

# Exception handling is a mechanism to handle runtime errors gracefully,
# preventing the program from crashing and allowing it to continue execution.

# 1. What are Exceptions?
# -----------------------
# Exceptions are errors that occur during the execution of a program.
# They disrupt the normal flow of the program.
# Examples: ZeroDivisionError, ValueError, FileNotFoundError, etc.

# 2. Basic Try-Except Block
# --------------------------
# The try block contains code that might raise an exception.
# The except block handles the exception if it occurs.

try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Cannot divide by zero!")

# 3. Catching Multiple Exceptions
# -------------------------------
# You can have multiple except blocks to handle different types of exceptions.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid integer!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    # Catch-all for any other exception
    print(f"An unexpected error occurred: {e}")

# 4. Using 'else' Clause
# ----------------------
# The else block executes if no exception occurs in the try block.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Division successful! Result: {result}")

# 5. Using 'finally' Clause
# -------------------------
# The finally block always executes, regardless of whether an exception occurred or not.
# Commonly used for cleanup operations (closing files, releasing resources).

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    # This will always execute
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened.")

# 6. Raising Exceptions
# ---------------------
# You can manually raise exceptions using the 'raise' keyword.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("You must be at least 18 years old!")
    else:
        print("Age is valid.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")

# 7. Creating Custom Exceptions
# -----------------------------
# You can create your own exception classes by inheriting from the Exception class.

class InsufficientFundsError(Exception):
    """Raised when there are insufficient funds for a transaction."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds. Balance: {balance}, Required: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)

# 8. Common Built-in Exceptions
# -----------------------------
# - ValueError: Raised when a function receives an argument of the right type but inappropriate value
# - TypeError: Raised when an operation or function is applied to an object of inappropriate type
# - IndexError: Raised when a sequence subscript is out of range
# - KeyError: Raised when a dictionary key is not found
# - FileNotFoundError: Raised when a file or directory is requested but doesn't exist
# - ZeroDivisionError: Raised when division or modulo by zero takes place
# - AttributeError: Raised when an attribute reference or assignment fails

# 9. Best Practices
# -----------------
# - Be specific with exception types in except blocks
# - Use finally for cleanup operations
# - Avoid bare except clauses (except:) as they catch all exceptions including system exits
# - Don't use exceptions for normal flow control
# - Provide meaningful error messages
# - Log exceptions for debugging purposes

# Example: Comprehensive Exception Handling
def safe_division(a, b):
    """
    Performs division with comprehensive error handling.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Division operation completed.")

# Test the function
print(safe_division(10, 2))  # Should work
print(safe_division(10, 0))  # ZeroDivisionError
print(safe_division(10, "2"))  # TypeError
