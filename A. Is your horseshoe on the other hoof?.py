col=list(map(int,input().split()))
x=set(col)
if len(x)==3:
    print(1)
elif len(x)==2:
    print(2)
elif len(x)==1:
     print(3)
else:
    print(0)
