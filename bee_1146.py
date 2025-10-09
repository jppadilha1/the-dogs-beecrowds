while True:
    x = int(input())
    if x == 0:
        break

    result = ''
    for i in range(1,x+1):
        if i == x:
            result += str(i)
        else:
            result += str(i) + ' '
    print(result)    
