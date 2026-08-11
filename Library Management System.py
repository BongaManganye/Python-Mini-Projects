# Library Management System
# Create a Book class and a Library class. The Library should store a list of books, allow adding books,
# Checking out books by title, and returning books

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append({"title": title, "availabe": True})

    def checkout(self, title):
        for b in self.books:
            if b["title"] == title and b["available"]:
                b["availabke"] = False
                return True
            return False
