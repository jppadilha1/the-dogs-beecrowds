n = int(input())
vel = list(map(int, input().split()))

idx = 0
for i in range(n - 1):
    if vel[i + 1] < vel[i]:
        idx = i + 2  # Convert to 1-indexed position
        break

print(idx)