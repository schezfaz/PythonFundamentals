"""
Naming Special Functions

Dunder functions: __feature__
- double underscore functions, make them distinct

Instance Attributes:
Assigned on a per object basis, usually in the __init__() method of a class

from attributes import *
c1 = ShippingContainer("Schez",["games"])
c1.owner_code
>>'Schez'
c1.contents
>>['games']

c1 is the instance of the class, owner_code and contents are instance attributes
each object/instance will have its own instance attributes

Class Attributes: Attributes associated with the class and not instance of the class
i.e. attribute whose value is shared by all instances of that class, defined within body of class

from attributes import *
--> retrive class attribute from outside the class: ShippingContainer.next_seial
or from the instances: c5.next_serial as all class attributes are attributes of all class instances as well

augmented operation (+=) is not an assignment, but a read/write/modify operator

"self" is an instance object reference i.e. print(self.instanceattribute)

Class Blocks/Blocks in general do not introduce scopes in python i.e. There is no class scope

Python Scoping Rules: LEGB
L: Local - inside the current function
E: Enclosing  - inside enclosing functions
G: Global - at the top level of any module
B: Built-in - in the special builtins module

Leading Underscore functions: _implementationFunction()
--> Leading underscore functions are implementation details of the class i.e. not intended for use outside

We would like to associate the implementation method with the class and not the instances of the class
There are 2 ways to achieve this:
    1. Static Method Decorator
    2. Class Methods
To create a static method, user @staticmethod decorator and remove the self parameter from the implementation function

Static methods do not have any knowledge of the class in which they are defined. They simply allow us to group a function within the class block, when the implementation of the function is related to the class level and not the instance level

ClassMethod: decorator: @classmethod
first argument by default is the class object: cls (analogous to the self keyword in instance methods)

Choosing @classmethod vs @staticmethod

@classmethod:
-> Requires access to class obj to class other class methods/constructor

@staticmethod:
-> No access needed to either class or instance objects
-> most likely an implementation detail of the class (leading underscore methods)
-> May be able to be moved outside the class to become a global scope func in the module without any loss of functionality

Named Constructor: Factory Functions i.e. constructs an object with certain configurations
Can call the factory method directly instead of calling the constructor

**kwargs are used to allow subclasses to thread arguements to base class dunder init and other mehtods

PROPERTIES: encapsulate getter() and setter() methods, properties behave like attributes

self._celcius: _celcius to indicate that this variable is no longer to be considered as part of the public interface

@property decorator: GETTER I.E.  read only attributes

@property
def celcius(self):
    return self._celcius

when r4.celcius: property decorator allows method to function like an attribute

@celcius.setter //decorator attribute
def p(self,value):
    self._p =value

self encapsulation: even properties of the class go through setter and getter validation
i.e. self._celcius can be written as self.celius

too many properties can lead to excessive coupling


"""

class ShippingContainer:
    next_serial = 69  #class attribute

    #def _generate_serial(self): #implementation detail of this class
    #def _generate_serial(self): argument self: first instance on which the method will operate


    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial #will refer to class atrribute
        cls.next_serial += 1
        return result

    #factory function to create an empty instance i.e. container of the class
    @classmethod
    def create_empty(cls, owner_code): #basically creates an empty shipping container having only serial number
        return cls(owner_code, contents=[])

    #factory function to create an obj to place iterable series of items in the container
    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents): #do nothing initialiser
        self.owner_code = owner_code #instance attribute
        self.contents = contents #instance attribute
        self.serial = ShippingContainer._generate_serial()
        #self.serial = ShippingContainer.next_serial #reference to class attribute from class object since it will be at the global/module scope
        #ShippingContainer.next_serial += 1

        #self.next_serial +=1 would create a new self attribute of the instance and overwrite the class attribute
        #instance attributes take precedence over class attribute while reference through self

        #self.serial = self._generate_serial() --> calling instance method via instance












