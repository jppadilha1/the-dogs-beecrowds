i = 0
positive = 0
while i < 6:
    x = float(input())
    if x > 0:
        positive += 1
    i+=1
print(f'{positive} valores positivos')