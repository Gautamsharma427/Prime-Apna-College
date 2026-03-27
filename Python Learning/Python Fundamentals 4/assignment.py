#1.

class BankAccount:
    def __init__(self,account_number,owner_name,balance):    
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        self.balance = self.balance - amount
    def check_balance(self):
        print(self.balance)

A = BankAccount(389283,"Ram",25000)
A.check_balance()
A.deposit(32000)
A.check_balance()
A.withdraw(3000)
A.check_balance()

#2 
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.list_of_reviews = []
    def add_review(self,review):
        self.list_of_reviews.append(review)
    def count_review(self):
        print(len(self.list_of_reviews))
    def display_all_reviews(self):
        for review in self.list_of_reviews:
            print(review)
HarryPotter = Book("Harry Potter","JK Rowling")
HarryPotter.add_review("Great BOOK")
HarryPotter.add_review("NICE BOOK")
HarryPotter.add_review("Average BOOK")
HarryPotter.display_all_reviews()
HarryPotter.count_review()

#3
class Student:
    def __init__(self):
        self.__name =" "
        self.__roll_no = 0
        self.__marks = 0
    def set_name(self,name):
        if(name.strip() == ""):
            print("Entering a name is compulsory")
        else:
           self.__name = name
    def set_roll_no(self,rollno):
        if(0<rollno<100):
            self.__roll_no = rollno
        else:
            print("ROLL NO can only be between 1 and 100")
    def set_marks(self,marks):
        if(marks>=0):
            self.__marks = marks
        else:
            print("MARKS CAN\"T BE NEGATIVE")
    def get_marks(self):
        return self.__marks
    def get_name(self):
        return self.__name
    def get_rollno(self):
        return self.__roll_no

Mark = Student()
Mark.set_name("Mark Zuckerberg")
Mark.set_roll_no(32)
Mark.set_marks(100)
print(Mark.get_marks())
print(Mark.get_name())
print(Mark.get_rollno())

#4
from abc import ABC,abstractmethod
class shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
circle = Circle(3)
print(circle.area())

class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
rectangle = Rectangle(2,3)
print(rectangle.area())
print(rectangle.area())
class Triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
triangle = Triangle(3,2)
print(triangle.area())

#5
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
class bike(Vehicle):
    def __init__(self,brand,model,cc):
        super().__init__(brand,model)
        self.engine_cc = cc
class car(Vehicle):
    def __init__(self,brand,model, seats):
        super().__init__(brand,model)
        self.seats = seats

#6
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class intern(employee):
    def __init__(self,stipend):
        self.stipend = stipend
    def calculate_salary(self):
        return self.stipend
class Fulltimeemployee(employee):
    def __init__(self,salary):
        self.salary = salary
    def calculate_salary(self):
        return self.salary
class Contract_based(employee):
    def __init__(self,wage,hours):
        self.wage = wage
        self.hours_worked = hours
    def calculate_salary(self):
        return self.wage * self.hours_worked
shyam = Contract_based(200,9)
print(shyam.calculate_salary())

#7
class Person:
    # We set age and address to None by default
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

# --- Testing the "Simulated Overloading" ---

# 1. Name only
p1 = Person("Alice")

# 2. Name + Age
p2 = Person("Bob", 25)

# 3. Name + Age + Address
p3 = Person("Charlie", 30, "123 Python Lane")

p1.display()
p2.display()
p3.display()

#8
class Player:
    player_count = 0
    def __init__(self,name,level):
        Player.player_count+=1
        self.name = name
        self.level = level
    def players(self):
        return Player.player_count
ram = Player("ram",23)
shyam = Player("shyam",57)
print(shyam.players())

#9
class herbivore:
    def eat(self):
        print("I eat plants")
class carnivore:
    def eat(self):
        print("I eat meat")
class omnivore:
    def eat(self):
        print("I eat both plants and meat")
class bear(herbivore,carnivore,omnivore):
    def __init__(self):
        omnivore.eat(self)
b = bear()
b.eat()

# 10
# ------------------------------
# 1. Message Class
# ------------------------------
class Message:
    # Class Attribute: Shared across all messages to ensure unique IDs
    message_counter = 1   

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        # Increment the shared counter every time a message is created
        Message.message_counter += 1

    def __str__(self):
        """Returns a formatted string representation of the message."""
        return f"[{self.id}] {self.sender.username}: {self.content}"

# ------------------------------
# 2. User Class
# ------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        """Connects the user to a specific chatroom."""
        if self.chatroom:
            print(f"❌ {self.username} is already in a chatroom ({self.chatroom.name}).")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"✅ {self.username} joined '{chatroom.name}'")

    def leave_chatroom(self):
        """Disconnects the user from their current chatroom."""
        if not self.chatroom:
            print(f"⚠️ {self.username} is not in any chatroom.")
        else:
            room_name = self.chatroom.name
            self.chatroom.remove_user(self)
            self.chatroom = None
            print(f"🚪 {self.username} left '{room_name}'")

    def send_message(self, content):
        """Sends a message to the currently joined chatroom."""
        if not self.chatroom:
            print(f"🚫 {self.username} cannot send message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)

# ------------------------------
# 3. ChatRoom Class
# ------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []      # List of User objects
        self.messages = []   # List of Message objects

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        """Creates a Message and 'sends' it to the room."""
        new_msg = Message(sender, content)
        self.messages.append(new_msg)
        print(new_msg)  # Real-time display

    def show_chat_history(self):
        """Prints all messages sent in this room."""
        print(f"\n--- Chat History: {self.name} ---")
        if not self.messages:
            print("No messages yet.")
        for msg in self.messages:
            print(msg)
        print("-" * (20 + len(self.name)) + "\n")

# --------------------------------------
# Example Usage
# --------------------------------------
if __name__ == "__main__":
    # Create the Room
    lounge = ChatRoom("Python Lounge")

    # Create Users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Users Join
    alice.join_chatroom(lounge)
    bob.join_chatroom(lounge)

    # Conversation starts
    alice.send_message("Hello everyone!")
    bob.send_message("Hi Alice! Ready to code?")

    # A third person joins mid-chat
    charlie.join_chatroom(lounge)
    charlie.send_message("Hey guys, what did I miss?")

    # View full history
    lounge.show_chat_history()

    # Users leave
    alice.leave_chatroom()
    bob.leave_chatroom()
    charlie.leave_chatroom()
