a1, a2, a3, a4 = map(int, input().split())
n = input()

tol = 0

for c in n:
    if  c== '1':
        tol += a1
    elif c == '2':
        tol += a2
    elif c == '3':
        tol += a3
    elif c == '4':
        tol += a4

print(tol)
