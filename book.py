class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def show(self):
        print(f"Title: {self.title}, Author: {self.author}, Year:{self.year}")

bookObject = Book("Python Programming" "Danny Onah", 2026)
bookObject.show()