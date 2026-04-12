

#01 check even and odd number
num=int(input("enter the number to check even and odd"))
if(num%2==0):
    print("even number",num)
else:
    print(num,"not even but odd number")

#02 check even and odd number using function
def even_odd(num):
    if(num%2==0):
        print("even number",num)
    else:
        print(num,"not even but odd number")

#02 check even and odd number using for loop
for i in range(1,11):
    if i % 2 == 0:
        print(i,"even numbeer")
    else:
        print(i,"odd number")