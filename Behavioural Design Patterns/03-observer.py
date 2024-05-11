"Observer Design Pattern Concept"


"""
Observar is a type of Behavioral Design Patterns

The Observer pattern is a software design pattern in which an object, called the Subject (Observable),
 manages a list of dependents, called Observers, and notifies them automatically of any internal state 
 changes by calling one of their methods.
"""

"""
Source Code
A Subject (Observable) is created.

Two Observers are created. 

The Subject notifies the Observers.

One of the Observers unsubscribes,

The Subject notifies the remaining Observer again.
"""




from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    "The Subject Interface"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "The notify method"

class Subject(IObservable):
    "The Subject (Observable)"

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)

class IObserver(metaclass=ABCMeta):
    "A method for the Observer to implement"

    @staticmethod
    @abstractmethod
    def notify(subject, *args):
        "Receive notifications"

class Observer(IObserver):
    "The concrete observer"

    def __init__(self, subject):
        subject.subscribe(self)

    def notify(self, *args):
        print(f"Observer id:{id(self)} received {args}")

# The Client
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)

SUBJECT.notify("First Notification", [1, 2, 3])

SUBJECT.unsubscribe(OBSERVER_B)
SUBJECT.notify("Second Notification", {"A": 1, "B": 2, "C": 3})