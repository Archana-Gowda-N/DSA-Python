#1. Addition, Subtraction, Multiplication, Division
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("the sum is:",n1+n2)
print("the difference is:",n1-n2)
print("the product is:",n1*n2)              
print("the quotient is:",n1/n2 if n2!=0 else "not defined")

#Even or Odd
n=int(input("enter the number to check even or odd"))
if n%2==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")

#Factorial
n=int(input("enter the number to find factorial"))
fact=1
for i in range(1,n+1):
    fact*=i
print("the factorial of",n,"is:",fact)

#Power (x^y)
n=int(input("enter the base number"))
p=int(input("enter the exponent"))
result=n**p
print("the result of",n,"raised to the power of",p,"is:",result)

#Square & Cube
n=int(input("enter the base number"))

result=n*n
rest=n*n*n
print("the square of",n,"is:",result)
print("the cube of",n,"is:",rest)

#Prime Number
n=int(input("enter the number to check prime or not"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")

    #7. GCD (HCF)

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print("the GCD of",num1,"and",num2,"is:",gcd(num1,num2))

#Armstrong Number
num=int(input("enter the number to check armstrong or not"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

    


