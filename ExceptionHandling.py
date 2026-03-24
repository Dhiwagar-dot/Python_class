try:
    age = int(input("Enter your age: "))
    result = 100 / age
except ValueError:
    print("Invalid input! Please enter a valid integer for age.")
except ZeroDivisionError:
    print("Age cannot be zero. Please enter a valid age.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:    print(f"Your age is {age} and the result of 100 divided by your age is {result}.")
finally:    print("Thank you for using the age calculator.")