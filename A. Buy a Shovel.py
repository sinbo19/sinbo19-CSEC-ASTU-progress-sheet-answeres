k, r = map(int, input().split())

count = 1
while True:
    if (k * count) % 10 == 0 or (k * count) % 10 == r:
        print(count)
        break
    count += 1
