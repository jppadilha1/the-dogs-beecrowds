n1, n2, n3 = map(int, input().split())

x = [n1, n2, n3]

y = sorted(x)

for i in range(3):
    print(y[i])

print()

for i in range(3):
    print(x[i])
