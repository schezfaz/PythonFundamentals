"""
Positional Arguments: matched with formal arguments by position, in order
Keyword Arguments: matched with formal arguments by name, any order

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
