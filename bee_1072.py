n = int(input())

qt_in = 0
qt_out = 0


for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        qt_in += 1
    else:
        qt_out += 1

print(f'{qt_in} in')
print(f'{qt_out} out')
