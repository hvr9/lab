def remove(arr):
    last=[]
    for i in arr:
        if i not in last:
            last.append(i)
    return last 
    
arr=[1,2,3,4,2,3,5]
print(arr)
arr2=remove(arr)
for k in range(0,len(arr2)):
    print(arr2[k])

