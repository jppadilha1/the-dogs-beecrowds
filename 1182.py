op = input()
matriz = [[],[],[],[],[],[],[],[],[],[],[],[]]
result = []

for i in range(12):
    for j in range(12):
        n = float(input())
        matriz[i].append(n)

        if j == col:
            result.append(n)

if op.lower() == 's':
    print(f'{sum(result):.1f}')
elif op.lower() == 'm':
    print(f'{(sum(result) / len(result)):.1f}')