a,b,c,d = map(int,input().split())

def validation():
    qt = 0
    if b>c and d > a:
        qt+=1
    if c+d > a+b and c>0 and d > 0:
        qt+=1
    if a % 2 == 0:
        qt+=1
    
    if qt == 3:
        return True
    else:
        return False

if validation():
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
