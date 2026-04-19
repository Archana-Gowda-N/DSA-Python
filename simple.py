n = input("Enter the number: ")
count = 0

for i in n:
    count += 1

print(count)

#02 HCF
n=int(input("enter the number"))
m=int(input("enter the number"))
greater=max(n,m)
while True:
   if greater%n==0 and greater%m==0:
       print(greater)
       break
   greater += 1
 
 #03 LCM  
a=int(input("enter the number"))
b=int(input("enter the number"))
a,b=b,a%b
print(b)

#04 random numbers 
import random
print("Random number:", random.randint(1, 100))







