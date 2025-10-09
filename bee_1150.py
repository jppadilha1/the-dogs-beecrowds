x = int(input())

z = int(input())

while z <= x:
    z = int(input())

qtd = 0
i = x
soma = 0
while soma <= z:
    soma += i
    qtd += 1   
    i += 1

print(qtd)