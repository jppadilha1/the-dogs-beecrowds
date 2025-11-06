def fat(n):
    if n < 2:
        return 1
    return n * fat(n-1)

while True:
    try:
        n1,n2 = map(int,input().split())

        print(fat(n1)+fat(n2))

    except EOFError:
        break