n = int(input())
s = input()

d = s.count("D")
a = s.count("A")

if a == d:
    print("Friendship")
elif a < d:
    print("Danik")
else:
    print("Anton")
