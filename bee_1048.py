x = float(input())

reajuste = 0.0
percentual = 0

if x <= 400.00:
    reajuste = x * 0.15
    percentual = 15
elif x <= 800.00:
    reajuste = x * 0.12
    percentual = 12
elif x <= 1200.00:
    reajuste = x * 0.10
    percentual = 10
elif x <= 2000.00:
    reajuste = x * 0.07
    percentual = 7
else :
    reajuste = x * 0.04
    percentual = 4


reajustado = x + reajuste
print(f'Novo salario: {reajustado:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')