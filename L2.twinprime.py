n=int(input("Enter limit : "))

def TwinPrime(h:int):
    flag=0
    for i in range(2,int((h/2)+1)):
        if (h%i)==0:
            flag=1
            break
    if flag==1:
        return False
    else:
        return True
    
for i in range(2,n):
    if i+2<n:
        if (TwinPrime(i)==True) and (TwinPrime(i+2)==True):
            print("(",i," ,",i+2,")")
