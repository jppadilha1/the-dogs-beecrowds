n = int(input())

i = 0
while i < n:
    result = ''
    str1, str2 = map(str, input().split())

    len_min = min(len(str1),len(str2))

    if len_min == len(str1):
         str_min = str1
    else:
         str_min = str1

    for i in range(len(str_min)):
        result += str1[i]
        result += str2[i]
    
    if str_min == str1:
        for i in range(len(str_min), len(str2)):
            result += str2[i]
    for i in range(len(str_min), len(str1)):
            result += str1[i]

    print(result)
    i+=1
        
## RUNTIME ERROR 