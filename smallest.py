a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if (a<=b) and (a<=c):
    small=a
elif (b<=a) and (b<=c):    
    small=b
else :
    small=c
print("smallest number is",small)    