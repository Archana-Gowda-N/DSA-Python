# n = int(input("Enter number of rows: "))

marks=[]

for i in range(5):
    n = int(input("Enter number of rows: "))
    marks.append(n)
marks1=max(marks)
marks2=min(marks)

avg=sum(marks)/len(marks)
print(avg)


for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)


for i in range(1,101):
    print(i)
    
for i in range(1,20,2):
    print(i)
    
for i in range(1,20,1):
    print(i)
    
for i in range(1,11):
    print(1,"x",i,"=",i*1)
 
sum=0   
for i in range(1,10,2):
    sum+=i
print(sum)

sum=0   
for i in range(1,10,1):
    sum+=i
print(sum)

n=int(input("enter the positive integer"))
count=0
while(n>0):
    digit=n%10
    count+=digit
    n=n//10
    
print(count)

n=int(input("enter the positive integer"))
while(n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
    
print(reverse)

    
    
