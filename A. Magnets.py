n = int(input())
previous = input()
groups = 1

for i in range(1, n):
    current = input()
    if current != previous:
        groups += 1
    previous = current

print(groups)
