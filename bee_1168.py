n = int(input())

leds = {"1":2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}

for i in range(n):
    num = input()
    total = 0
    for digit in num:
        total += leds[digit]
    print(f'{total} leds')

