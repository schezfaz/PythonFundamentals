"""
Positional Arguments: matched with formal arguments by position, in order
Keyword Arguments: matched with formal arguments by name, any order

Fucntions are defined at runtime

Functions are first class. i.e. functions are objects and can be passed around

__call__(): Allow objects/instaces of classes to be callable objects
--> invoked on objects when they are called like functions

callable(function_name): inbuilt function to check whether func. is callable or not

Lambda functions: to create simple callable objects  i.e. anonymous callable objects

Lambda is an expression which results in a callable object

syntax: lambda args: expr
def name(args): body

*args: n number of arguments in the form of a tuple

When the function accepts a variable number of arguments with a postive lowerbound, use regular arguments for the required parameters and *args for the balance of parameters
*args should come after regular positional arguments, only 1 occurence in the argument intake
it only collects positional arguments

Arbitrary keyword arguments: **kwargs --> can be any name preceeded by double asterix **

Order of args: *args should always come before **kwargs
Any arguments before *args are treated as regular positional arguments
any regular args after *args must be passed as compulsory keyword arguments

Situation in which you need to use mandatory keyword arguments without accepting arbitrary number of positional arguments:
--> omit name of *args argument, and everything after the  * will be treated as a keyword argument

**kwargs should always be last in the func parameter list

Position only arguments: use / python 3.8 and later:
def number_length(x,/):
    pass

i.e. x can only be passed positionally, and not via number_length(x=value) keyword

"""

scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin','Niels Bohr', 'Dian Fossey','Grace Hopper','Charles Darwin']
print(sorted(scientists, key = lambda name: name.split()[-1])) #passing lambda function as key argument

#lambda accepts a single argument 'name' and body of the lambda is after the colon

def hypervolume(*args):
    print(args)
    print(type(args))

# hypervolume(3,4)

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

# print(hypervolume(3,4))

#HTML tag function: accepts name of the tag + attributes of tag
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result +='>'
    print(result)

# tag('img',src="schez.jpg",alt="peepeepoopoo")

"""
Extended Call Syntax:  allows us to use iterable series like tuple to populate positional arguments and any mapping type such  as a dictionary that has string keys to populate keyword args

Argument forwarding: *args and **kwargs are used to forwards all arguments of a function to another function

"""

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

t = (11,12,13,14)
print_args(*t) #* is used to instruct python to unpack the series into positional arguments

#each of the 3 args i.e. red, green, blue can be used as positional or keyword args at the callsite
def colour(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print(kwargs)

k = {'red':21,'green':68, 'blue': 120, 'alpha' : 52}
colour(**k)

'''
Functions defined inside other functions: local functions
i.e. there will be a new copy of the function made for each enclosing invocation

Local functions are not 'members' of their enclosing functions, they are just local name bindings in the function body
Local functions help with code readibality and organisation similar to lambdas, more general than lambdas

First class functions: (Returning functions) : where functions can be passed to and returned from other functions/ treated as any piece of data
Once the local function is returned, the enclosing scope is gone along with any objects it has defined

Closure: Records objects from enclosing scopes: Closure remembers the objects from the enclosing scope that the function will need, it keeps the recorded objects alive for use after the scope is gone

The local function closes over the objects it needs, preventing them from being garbage collected

Implements closure with special attribute: __closure__

Function Factories: Functions that return other functions, returned functions use both their own arguments as well as arguments passed to the function factory

'''

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sort_by_last_letter(strings, key=last_letter)

# print(sort_by_last_letter(['Schezeen','Fazulbhoy','Peepeepoopoo']))

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l)
    inner()

# outer()

#returning local functions

def enclosing():
    def local_func():
        print('local func waddup')
    return local_func()

enclosing()

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(square.__closure__)
print(square(5))

message = 'global'

'''
Name binding in enclosing scope: in local() we are creating a new name binding in that scope
it will only be present in that scope and not anywhere else

global keyword: introduces bindings from the global scope into another scope

nonlocal keyword: inserts a name binding from an enclosing scope to the local namespace

'''
def enclosing():
    message = 'enclosing'

    def local():
        global message #once this is done, and local() is called, the global binding will be updated
        message = 'local' #only present in this scope

'''
function decorators: modify or enhance an existing function in a non-intrusive and maintainable way
--> implemented as a callable that accepts a callable and returns a callable
i.e. functions that accept a function as an argument and return a function

f is the parameter to escape_unicode: f is the function that needs to be decorated
local function: wrap --> accepts any number of arguments
it then calls f i.e. the input function with the arguments received
wrap will behave just like f i.e. decorated function and will return only ascii characters

'''

#decoartor function
def escape_unicode(f):
    def wrap(*args,**kwargs):
        x = f(*args,**kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def some_city():
    return 'Mumbai~Ø'

print(some_city())

'''
Classes as Decorators: Classes are callable objects
--> Functions decorated with a class are replaced by an instance of the class because the function to be decorated will be passed to the constructor and thus the initialiser

Object returned from the decorated must be a callable i.e. the instance resulting from the constructor must be callable i.e. it must support __call__() method

Class Decorators are useful for attaching some extra data to functions
'''

class CallCount:
    def __init__(self,f):
        self.f = f #takes input function f and initialises it as a member attribute
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count +=1
        return self.f(*args,**kwargs) #returns whatever value f i.e. decorated function produces

@CallCount
def hello(name):
    print('Hello, {}!'.format(name))

hello("Schez")
hello("Chris")

print(hello.count)




