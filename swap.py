#01 
a,b,c=10,20,30
print("Before swapping: ",a,b,c)
a,b,c=c,a,b
print("After swapping: ",a,b,c)

#02(using temporary variable)
a,b,c=10,20,30
print("Before swapping: ",a,b,c)
temp=a
a=c
c=b
b=temp
print("After swapping: ",a,b,c)
#03(using temporary variable)
a=10
b=20
temp=a
a=b
b=temp
print("After swapping: ",a,b)

#04 (without using temporary variable )
a=10
b=20
print("before swaping ",a,b)
a=a+b
b=a-b
a=a-b
print("after swap",a,b)

#04 swaping using XOR method

a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)