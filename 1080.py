i = 2
n_index = {}
first = int(input())
n_index[first] = 1
maior = first

while i <= 100:
    n = int(input())
    n_index[n] = i

    if n > maior:
        maior = n

    i+=1

print(maior)
print(n_index[maior])