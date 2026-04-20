#looping

for i in range(1,10):
    print(i)
    
for i in range(10,0,-1):
    print(i,end=" ")

#print even numbers from 1 to 50
print("even numbers")
for i in range(2,50,2):
    print(i,end=" ")

#Print odd numbers from 1 to 50
for i in range(1,50,2):
    print(i,end=" ")
    
#Print multiplication table of a number
for i in range(1,11):
    print(2,"x",i,"=",2*i)
    
#Find sum of first N natural numbers
# Find factorial of a number
# Count number of digits in a number
# Reverse a number
# Check palindrome number

n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
    sum+=n
    # n=n//10
print(sum)

#02
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

n=int(input("enter the number"))
count=0
for i in range(1,n+1):
    digit=n%10
    count+=digit
    # n//=10
print(count)

n=int(input("enter the number"))
for i in range(n,0,-1):
    print(i)

n=input("enter the number")
if n[::-1]==n:
    print("palindrome")
else:
    print("not a palindrome")




    
