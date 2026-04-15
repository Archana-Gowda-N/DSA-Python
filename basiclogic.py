# factorial of recurrsion 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the number to find its factorial"))
print("factorial of the number is",factorial(num))

#multiplication table
def multiplication_table(n):
    print("multiplication table of",n)
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

num=int(input("enter the number to find its multiplication table"))
multiplication_table(num)

#natural numbers
n=int(input("enter the number of natural numbers to find their sum"))
n=n*n+1//2
print("the result is",n)

#reverse of numbers
num=int(input("enter the number to find its reverse"))
reverse=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("reverse of the number is",reverse)

