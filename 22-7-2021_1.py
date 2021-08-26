s=list(map(str,input().split()))
k=[]
f=[]
l=[]
for i in range(len(s)):
    if 'e' in s[i]:
        j=s[i]
        c=j.count('e')
        k=j.split("e")
        if(c<2):
            f.append(k[0])
            l.append(k[1])
        else:
            f.append(k[1])
            l.append(k[2])
print(f,l)