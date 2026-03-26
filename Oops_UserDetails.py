class User:
    id = 1
    first_name = ""
    last_name = ""
    email = ""
    password = ""
    is_active = True
User1 = User()
print(User1)

User1.first_name = "Dhiwagar"
User1.last_name = "S"
User1.email = "dhiwagar22@gmail.com"
print(User1.first_name)
print(User1.last_name)
print(User1.email)
User1.age = 30
print(User1.age)