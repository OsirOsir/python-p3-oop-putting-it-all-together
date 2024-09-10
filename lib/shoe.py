#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9):
        self._brand = brand
        self._size = size
        self.condition = "Used"
        
    @property
    def brand(self):
        print("Getting shoe brand")
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        print(f"The set shoe brand is {brand}")
        self._brand = brand
        
    @property
    def size(self):
        print("Getting shoe size")
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            print(f"The set shoe size is {size}")
            self._size = size
            
        else:
            print("size must be an integer")
            
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    
