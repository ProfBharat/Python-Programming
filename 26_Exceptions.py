# Python program to show Exception handling
a = 1000030
b = 300
# put b= 0 and try to execute
try:
    x = a//b

except ZeroDivisionError:
    print("we can 't divide with zero")
except NameError:
    print("Name Error by writing manoj")
else:
    print("The value of x is :",x)

finally:
    print(" Remember do not tried to divide with zero")

