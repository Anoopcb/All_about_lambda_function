# lambda expressions, or anonymous function
def add_one(a,b):
    return  a+b
## make this function by lambda expression

add_two = lambda  a,b : a+b## normally we do not asign lambda in a variable


print(add_two(25, 75))

## we use lambda with built in function like, map, reduce, filter
multiply = lambda  a, b: a*b


print(multiply(25, 3))



is_even = lambda a: a%2==0
print(is_even(25))


last_char = lambda s: s[-1]
print(last_char("Anoop"))


## lambda with if, else

def func5(s):

    if len(s)>5:

        return True
    else:
        return False

    func6 = lambda s: True if len(s)>5 else False
    print(func6("Anoopsheoran"))



    func6 = lambda s: len(s)>5
    print(func6("Anoopsheoran"))








