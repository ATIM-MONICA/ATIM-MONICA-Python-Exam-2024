# 5. (i)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

# Creating the instance of the class
book = Book("Love Does", "Bob Golf", 281)
book.display_info()


# 5.(ii)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class EBook(Book):
    def __init__(self, title, author, pages, format):
    
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format} MB")

book = Book("Love Does", "Bob Golf", 281)
book.display_info()

ebook = EBook("Love Does", "George Orwell", 328, 1.5)
ebook.display_info()


# 5.(iii)
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
    
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_and_author(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, pages, format):
    
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
      
        super().display_info()
        print(f"Format: {self.format} MB")

book = Book("Love Does", "Bob Golf", 281)
book.display_info()
print(book.get_title_and_author())

ebook = EBook("Love Does", "George Orwell", 328, 2)
ebook.display_info()

# (iii)
def get_title_and_author(self):
 
    return (f"{self.title} by {self.author}")
book = Book("Love Does", "Bob Golf" , 281)
ebook = EBook("Love Does", "George Orwell", 328,2 )
print(book.get_title_and_author()) 
print(ebook.get_title_and_author())   
# 5. (iv)
#A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. A class encapsulates data (attributes) and behaviors (methods) into a single unit.
# EG
class Book:
#Object
# #An object is an instance of a class. It represents a specific entity with the attributes and behaviors defined by its class. Each object can have unique values for its attributes.

# # Example
 class Car:
    def __init__(self, make, model, year):
        self.make = make   # Attribute: make of the car
        self.model = model # Attribute: model of the car
        self.year = year   # Attribute: manufacturing year

    def display_info(self):
       return f"{self.year} {self.make} {self.model}"

 # Creating objects (instances) of the Car class
 car1 = Car("Toyota", "Corolla", 2020)
 

