# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class.
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
# First Class Objects
# In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.
# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

# def shout(text):
#     return text.upper()
#
#
# print(shout('hello'))
#
# yell = shout
# # by using function object reference created same functionality
# print(yell('how are u'))

# 2: Passing the function as an argument
# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(func):
#     greeting = func("Hi mahesh Welcome to developer of Wipro")
#     print(greeting)
# # passing the function as argument
# greet(shout)
# greet(whisper)


# 3. functions can return another function
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
# add_15 = create_adder(15)
# print(add_15(10))

# decorator chaining
# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())


