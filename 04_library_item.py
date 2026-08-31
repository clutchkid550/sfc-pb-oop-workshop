"""
You are tasked with developing a system to manage different types of media in a library.
The library contains various types of items such as books, magazines, and DVDs.
Each type of media shares some common attributes but also has specific attributes and behaviors unique to its type.
You will need multiple classes to accomplish this, with some classes inheriting from a parent class.
See example:
Once your classes are complete, copy and paste the above example below them in order to test their functionality.

Write a class that meets these requirements.
Name:       LibraryItem
Required state:
   * title, the title of the item
   * publication date, the date the item was published
   * identifier, a unique identifier for the item
Behavior:
   * get_info()     # Returns information about the item

"""
class LibraryItem:
    def __init__(self, title, pub_date, identifier):
        self.title = title
        self.pub_date = pub_date
        self.identifier = identifier

    def get_info(self):
        return(f'Title: {self.title}, Publication Date: {self.pub_date}, Identifier: {self.identifier}')

"""Write a class that meets these requirements.
Name:       Book (inherits from LibraryItem)
Required state:
   * author, the author of the book
   * pages, the number of pages in the book
Behavior:
   * get_info()     # Returns information about the book, including the author and number of pages
"""

class Book(LibraryItem):
    def __init__(self, title, pub_date, identifier, author, pages):
        super().__init__(title, pub_date, identifier)
        self.author = author
        self.pages = pages

    def get_info(self):
        return(f'Title: {self.title}, Publication Date: {self.pub_date}, Identifier: {self.identifier}, Author: {self.author}, Pages: {self.pages}')

""" Write a class that meets these requirements.
Name:       Magazine (inherits from LibraryItem)
Required state:
   * issue number, the issue number of the magazine
   * month, the month the magazine was published
Behavior:
   * get_info()     # Returns information about the magazine, including the issue number and month
"""
class Magazine(LibraryItem):
    def __init__(self, title, pub_date, identifier, issue_number, month):
        super().__init__(title, pub_date, identifier)
        self.issue_number = issue_number
        self.month = month

    def get_info(self):
        return(f'Title: {self.title}, Publication Date: {self.pub_date}, Identifier: {self.identifier}, Issue Number: {self.issue_number}, Month: {self.month}')

"""Write a class that meets these requirements.
Name:       DVD (inherits from LibraryItem)
Required state:
   * duration, the duration of the DVD in minutes
   * director, the director of the DVD
Behavior:
   * get_info()     # Returns information about the DVD, including the duration and director
"""
class DVD(LibraryItem):
    def __init__(self, title, pub_date, identifier, duration, director):
        super().__init__(title, pub_date, identifier)
        self.duration = duration
        self.director = director

    def get_info(self):
        return(f'Title: {self.title}, Publication Date: {self.pub_date}, Identifier: {self.identifier}, Duration: {self.duration} minutes, Director: {self.director}')

#TEST

book = Book("The Great Gatsby", "1925", "B001", "F. Scott Fitzgerald", 218)
magazine = Magazine("National Geographic", "2021", "M001", 12, "December")
dvd = DVD("Inception", "2010", "D001", 148, "Christopher Nolan")

print(book.get_info())         # Prints book information
print(magazine.get_info())     # Prints magazine information
print(dvd.get_info())          # Prints DVD information