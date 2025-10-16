start_hour, end_hour = map(int, input().split())

if start_hour < end_hour:
    duration = end_hour - start_hour
elif start_hour > end_hour:
    duration = 24 - start_hour + end_hour
else:  # start_hour == end_hour
    duration = 24

print(f"O JOGO DUROU {duration} HORA(S)")