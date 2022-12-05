a = 10
b = 20
c = 30
def add():
    print("addition of a,b:", a + b)
def greet():
    print("Hello, good morning friends")


def add_2( a,  b):
     sum = a + b
     return sum

def add_3( a,  b, c ):
     sum = a + b + c 
     return sum

add()   
greet()        #  a function without any parameters

print("The addition of a,b is :",add_2(a,b))
print("The addition of a,b,a is :",add_3(a,b,c))      # a function with two parameter
