n = int(input())
h = []
d = []
for i in range(n):
    k, a = map(int, input().split())
    h.append(k)
    d.append(a)

count = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if h[i] == d[j]:
                count += 1
print(count)
