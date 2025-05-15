#!/usr/bin/env python3


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if lib_book.title == book.title and lib_book.author == book.author:
                self.books.remove(lib_book)
                break

    def search_books(self, search_string):
        self.search_string(book)
