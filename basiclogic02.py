#01 .Find greatest of three numbers 
from turtle import left


num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if num1>num2 and num1>num3:
    print(num1,"is the greatest number")
elif num2>num1 and num2>num3:
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")

#02 Fibonacci series
n=int(input("enter the number of terms in fibonacci series"))
a=0
b=1
print("fibonacci series is:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
print()
#03 Check prime number
num=int(input("enter the number to check prime or not"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")

else:
    print(num,"is not a prime number")

#04 Sum of the digits of a number
num=int(input("enter the number to find the sum of its digits"))
#1234
sum=0
while num>0:    
    digit=num%10  #if we use num%10 refers last digit
    sum+=digit  # adding last to sum (0+4)
    num//=10 #removes the last digit
print("sum of the digits is:",sum)

#reverse of number
num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit  #*10 means shifting towords left side and +10 means addnnew digit
    num //= 10 # remove last digit

print("Reversed number:", reverse)
