"""concatenation of 2 arrays
Harsha vardhan 
121910313001"""
k=int(input("enter size of array 1:"))
list1=[]
for i in range(k):
    a=input("element:")
    list1.append(a)
p=int(input("enter size of array 2:"))
list2=[]
for i in range(p):
    b=input("element:")
    list1.append(b)
n=k+p
list3=[None]*(n)
list3=list1+list2 
print("New list is: ",list3)