x = int(input())
y = int(input())

i = 0
result = 0
if x > y:
    i = x-1
    while i > y:
        if i % 2 != 0:
            result += i
        i -= 1
else:
    i = y+1
    while i < x:
        if i % 2 != 0:
            result += i
        i += 1

print(result)