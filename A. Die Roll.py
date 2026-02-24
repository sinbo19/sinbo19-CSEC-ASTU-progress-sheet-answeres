y, w = map(int, input().split())
z = max(y, w)
k = 6 - z +1
total=6
if k == 0:
    print("0/1")
elif k == 6:
    print("1/1")
elif k == 3:
    print("1/2")
elif k== 2:
    print("1/3")
elif k == 1:
    print("1/6")
elif k== 4:
    print("2/3")
elif k == 5:
    print("5/6")
