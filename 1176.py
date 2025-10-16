cases = int(input())

def fibo(n):
    if n == 0 or n == 1:
        return n
    
    nums = [0,1]

    i = 0
    x = 0
    y = 1
    while i < n:
        nums.append(x+y)
        x, y = y, x+y
        i+=1
    
    return nums[n]


for i in range(cases):
    n = int(input())
    print(f'Fib({n}) = {fibo(n)}')
