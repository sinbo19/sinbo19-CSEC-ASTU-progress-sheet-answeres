k = input()
upper = 0
lower = 0
for n in k:
    if n.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(k.upper())
else:
    print(k.lower())
