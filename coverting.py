# 01.Convert Kilometers to Miles
 #formula: miles = kilometers * 0.621371
km=float(input("enter the distance in kilometers"))
miles = km * 0.621371
print("Distance in miles:", miles)

# 02. Calculate the area of a triangle
bas=float(input("enter the base of the triangle"))
height=float(input("enter the height of the triangle"))
area=(1/2*bas*height)
print("area of the triangle is",area)

# 03. Calculate the area of a circle
radius=float(input("enter the radius of the circle"))
area=3.14*radius*radius
print("area of the circle is",area)

#04. Perimeter of Rectangle
length=float(input("enter the length of the rectangle"))
width=float(input("enter the width of the rectangle"))
perimeter=2*(length+width)
print("perimeter of the rectangle is",perimeter)    

#05 .Square of a Number
num=int(input("enter the number to find its square"))
square=num*num
print("square of the number is",square)

#06.Cube of a Number
num=int(input("enter the number to find its square"))
cube=num*num*num
print("square of the number is",cube)

#07.Factorial (using loop concept)
num=int(input("enter the number to find its factorial"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial of the number is",factorial)

