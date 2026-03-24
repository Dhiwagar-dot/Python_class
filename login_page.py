user_details = [
    {"username": "john_doe", "password": "password123"},
    {"username": "jane_soe", "password": "securepass456"},
    {"username": "alice_smith", "password": "mypassword789"}
]

def login(username, password):
    for user in user_details:
        if user["username"] == username and user["password"] == password:
            return "Login successful!"
    return "Invalid username or password."

def main():
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    return login(username_input, password_input)

def login_system():
    count = 0
    max_attempts = 2

    while count < max_attempts:
        count += 1
        result = main()
        print(result)

        if result == "Login successful!":
            print("Welcome to the system!")
            break
        else:
            print(f"Attempt {count} of {max_attempts} failed. Please try again.")
    else:
        print("Maximum login attempts reached. Please try again later.")

# Run the program
login_system()
