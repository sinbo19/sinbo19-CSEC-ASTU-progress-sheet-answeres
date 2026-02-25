n = int(input())
crime = list(map(int, input().split()))
p = 0      
ch = 0     
 
for a in crime:
    if a == -1:
        if p > 0:
            p -= 1
        else:
            ch += 1
    else:
        p += a
 
print(ch)
