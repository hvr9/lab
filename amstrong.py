#amstrong number
n=int(input("enter the number:"))
count=0
dup=n
while dup>0:
    r=dup%10
    count+=r**3
    dup//=10
if(n==count):
    print("amstrong num")
else:
    print("not an amstrong num")    