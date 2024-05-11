# -*- coding: utf-8 -*-
"""
    The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex 
    object from its representation so that you can use the same construction process to create different 
    representations.
"""

"""
           Factory Vs. Builder
    The Builder and Factory patterns are very similar in the fact they both instantiate new objects at runtime.
    The difference is when the process of creating the object is more complex, so rather than the Factory
    returning a new instance of ObjectA, it calls the builders' constructor method ObjectA.construct()
    that goes through a more complex construction process involving several steps. Both return 
    an Object/Product.
"""
    
"Builder Concept Code"

from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)