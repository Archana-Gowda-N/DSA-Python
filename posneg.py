#01	Check positive or negative number 
num=int(input("enter the number to check positive or negative"))
if(num>0):
    print("positive number",num)
elif(num<0):
    print("negative number",num)
else:
    print(num,"is neither positive nor negative")