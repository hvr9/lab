#LCM OF TWO NUMBERS
x=int(input("enter number:"))
y=int(input("enter number:"))
if(x>y) :
    greater=x
else:
    greater=y
while(True):
    if(greater % x == 0) and (greater % y ==0):
        lcm = greater
        break
    greater += 1

print("LCM is",lcm)    6