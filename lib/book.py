#!/usr/bin/env python3

class Book:
    def __init__(self, title = "And Then There Were None", page_count = 272):
        self._title = title
        self._page_count = page_count
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!") 
        
    @property
    def title(self):
        print("Getting boom title")
        return self._title
    
    @title.setter
    def title(self, title):
        print(f"Book title: {title}") 
        self._title = title
        
    @property
    def page_count(self):
        print("Getting page count")
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            print(f"The set book's page count is {page_count}")
            self._page_count = page_count
        
        else:
            print("page_count must be an integer")
        
        
    
        
