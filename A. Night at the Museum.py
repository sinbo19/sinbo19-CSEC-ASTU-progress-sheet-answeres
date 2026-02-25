n=input()
s='a'
move=0
for i in n:
    different = abs(ord(i)-ord(s))
    move+=min(different,26-different) 
    s=i
print(move)
