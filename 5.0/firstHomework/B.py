g11, g21 = (map(int, input().split(":")))
g12, g22 = (map(int, input().split(":")))
location = int(input())

if location == 1:
    score1 = g11 * 100 + g12 * 101
    score2 = g21 * 101 + g22 * 100
    print(max(0, (score2 - score1 + 101) // 101))
else:
    score1 = g11 * 101 + g12 * 100
    score2 = g21 * 100 + g22 * 101
    print(max(0, (score2 - score1 + 100) // 100))