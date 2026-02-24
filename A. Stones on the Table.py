n=int(input())
z=input()
count=0
for i in range(n-1):
    if z[i]==z[i+1]:
        count +=1
print(count)
