while True:
    a, z = map(int, input().split())

    if a <= 0 or z <= 0:
        break

    if a > z:
        a, z = z, a
    

    soma = 0
    result = ''
    k = a
    while k <= z:
        soma += k
        result += f'{k} '
        k += 1

    result += f'Sum={soma}'
    print(result)
