def fact(n):
    temp=1
    for i in range(n,0,-1):
        temp=temp*i
    print("Factorial of",n,"is:",temp)

a=int(input("Enter a number to find factorial:"))
fact(a)