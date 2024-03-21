n = int(input())
vals = list(map(int, input().split()))
a, b, k = map(int, input().split())
minSect = (a - 1) // k
maxSect = (b - 1) // k
ans = -1
for j in range(2):
    usedSect = [False] * n
    for i in range(minSect, maxSect + 1):
        ans = max(ans, vals[i % n])
        if usedSect[i % n]:
            break
        usedSect[i % n] = True
    vals = [vals[0]] + vals[1:][::-1]
print(ans)