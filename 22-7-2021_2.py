l=list(map(int,input().split(",")))
n=len(l)
c=l.count(0)
print(sum(l)*n-c)