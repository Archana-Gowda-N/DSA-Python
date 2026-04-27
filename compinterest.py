p=int(input("enter the principal amount"))
r=int(input("enter the rate of interest"))
t=int(input("enter the time period"))
si=p*(1+(r/100)**t)
ci=si-p
print("simple interest is",si)
print("compound interest is",ci)

#02 check compound interest using function
def compound_interest(p,r,t):
    s=p*(1+(r/100)**t)
    c=s-p
    return s,c
p=int(input("enter the principal amount"))
r=int(input("enter the rate of interest"))
t=int(input("enter the time period"))
print("simple interest is",compound_interest(p,r,t)[0])
print("compound interest is",compound_interest(p,r,t)[1])


#convert celsius to fahrenheit
c = float(input("Enter temperature in Celsius: "))

f = (9/5) * c + 32

print("Temperature in Fahrenheit:", f)
