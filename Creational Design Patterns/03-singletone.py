
"""
   Singleton Method is a type of Creational Design pattern that makes sure that only one instance 
   of a class exists. such as db connection
"""

"""
   By creating a class and following the Singleton pattern, you can enforce that even if 
   any number of instances were created, they will still refer to the original class.
   The Singleton can be accessible globally, but it is not a global variable. It is a 
   class that can be instanced at any time, but after it is first instanced, any new
   instances will point to the same instance as the first.
   
   For a class to behave as a Singleton, it should not contain any references to self but use static 
   variables, static methods and/or class methods.
"""
    
"Singleton Concept Code"


import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")