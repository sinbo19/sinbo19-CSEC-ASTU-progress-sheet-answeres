n, h = map(int, input().split())

lis = list(map(int, input().split()))

val= 0

for i in lis:
    if i <= h:
        val += 1
    else:
        val += 2

print(val)
