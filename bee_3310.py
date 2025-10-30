size_fase = int(input())


fase1 = input().split()
fase2 = input().split()

i = 0
gravity = 0
while i != size_fase-1:
    if fase1[0] == '0' or fase1[0] == '2' or fase1[1] == '2':
        t = fase1.copy()
        fase2 = t
        fase1 = fase2.copy()
        gravity+=1

    if fase1[i+1] == '0' or fase1[i+1] == '2' and fase1[i] == '1':
        t = fase1.copy()
        fase2 = t
        fase1 = fase2.copy()
        gravity+=1
    i+=1

print(gravity)