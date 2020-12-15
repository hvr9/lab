arr1=[1,2,3,4,5,6]
arr2=[None]*len(arr1)
l=len(arr1)
for i in range(l):
    arr2[i]=arr1[l-i-1]
print(arr1)
print("new array is",arr2)    
