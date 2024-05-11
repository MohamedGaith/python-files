"""
Adapter is a type of ٍٍStructural Design Patterns

The Adapter is used when you have an existing interface that doesn't directly map to an interface 
that the client requires. So, then you create the Adapter that has a similar functional role, but
with a new compatible interface.
"""


class ClassA():
    "A Sample Class the implements IA"

    def method_a(self):
        print("method A")


class ClassB():
    "A Sample Class the implements IB"

    def method_b(self):
        print("method B")

class ClassBAdapter():
    "ClassB does not have a method_a, so we can create an adapter"

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()
        


# Before the adapter I need to test the objects class to know which
# method to call.
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# After creating an adapter for ClassB I can reuse the same method
# signature as ClassA (preferred)
ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()