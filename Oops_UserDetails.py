 # Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. In OOP, a class is a blueprint for creating objects, which are instances of the class. Each object can have attributes (data) and methods (functions) that operate on the data.
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

# Constructor is a special method in a class that is automatically called when an object of the class is created. It is typically used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.
class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.is_active = True
User1 = User(1, "Dhiwagar", "S", "dhiwagar22@gmail.com", "password123")
print(User1.id, User1.first_name.capitalize(), User1.last_name.capitalize(), User1.email, User1.password)
User2 = User(2, "John", "Doe", "john.doe@gmail.com", "password456")
print(User2.first_name)
User3 = User(3, "Jane", "Smith", "jane.smith@gmail.com", "password789")
print(User3.first_name)