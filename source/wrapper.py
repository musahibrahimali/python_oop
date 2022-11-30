
# create a decorator
def wrapper(func):
    def inner():
        print("Started")
        func()
        print("Ended")

    return inner


# use @f1 to decorate f2
@wrapper
def f2():
    print("Hello")


# call the decorated function
# f2()


# wrapper(f2)()

# x = wrapper(f2)  # function aliassing
# x()
# print the type of x
# print(type(x))
# f1(f2)()
# f2()

def swap(fun):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)

    return inner


@swap
def div(a, b):
    print(a / b)


div(4, 2)
