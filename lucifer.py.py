def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
number = int(input("Enter non negative integer number => "))
numfact = factorial(number)
print("Factorial of",number,"=",numfact)
