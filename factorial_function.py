def fact(n):
    result = n
    while n > 1:
        result *= (n-1)
        n -= 1
    return result
        
    
print(fact(8))