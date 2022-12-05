# python program to find the factorial of given number



number = int(input("Enter a number to find the factorial"))

def fact(number):
    return 1 if(number ==1 or number==0) else number * fact(number-1)

result = fact(number)
print(result)


