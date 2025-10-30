h, duration, fuse = map(int, input().split())

arrival_time = h + duration
if arrival_time > 24:
    arrival_time -= 24

if arrival_time+fuse < 0:
    print(24 + (arrival_time+fuse))
else:
    print(arrival_time+fuse)