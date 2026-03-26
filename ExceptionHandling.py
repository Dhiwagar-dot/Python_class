try:
    age = int(input("Enter your age: "))
    result = 100 / age
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
except ZeroDivisionError:
    print("Age cannot be zero. Please enter a valid age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Your age is {age} and the result of 100 divided by your age is {result}.")
finally:
    print("Thank you for using the age calculator.")

def check_length(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    return True
try:
    user_password = input("Enter your password: ")
    if check_length(user_password):
        print("Password is valid.")
except ValueError as ve:
    print(f"Error: {ve}")

users = [{name: age} for name, age in [("Alice", 30), ("Bob", "unknown"), ("Charlie", 25)]]    

for user in users:
    try:
        for name, age in user.items():
            print(f"{name} is {age} years old.")
    except Exception as e:
        print(f"An error occurred while processing user data: {e}") 