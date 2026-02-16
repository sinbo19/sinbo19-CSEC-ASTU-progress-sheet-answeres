n = int(input())
count = 0
for i in range(n):
    a, b, d = map(int, input().split())
    
    if a + b + d >= 2:
        count += 1
print(count)
