"""
Everything is an object in python

Classes: Define structure and behaviour of objects
Act as a template for creating new objects and control an object's initial state, attributes and methods

class ClassName: follow Pascal case

methods are functions defined inside a class
instance methods: methods that can be called on an instance of a class
instance methods must accept a reference to the actual instance on which the method was called as first argument i.e. 'self'

 from classes import Flight
 f = Flight()
 f.number() ==> Flight.number(f) that is why we dont pass f to the function self as it is a shorthand for this actual notation


"""

class Flight:
    def number(self):
        return "SN060"