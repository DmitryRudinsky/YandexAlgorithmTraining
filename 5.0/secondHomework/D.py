N = int(input())
coordinates = [tuple(map(int, input().split()))for _ in range(N)]
P = 0
for coordinate in coordinates:
    x, y = coordinate
    directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for direction in directions:
        if direction not in coordinates:
            P += 1
print(P)