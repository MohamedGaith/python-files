"""
    Factory Method is a Creational Design Pattern that allows an interface or a class to create an object,
    but lets subclasses decide which class or object to instantiate.
"""

"The Factory Concept"
    

class ConcreteProductA():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"



class ConcreteProductB():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"



class ConcreteProductC():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"



class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)