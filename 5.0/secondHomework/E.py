n = int(input())
maxGoodI = -1
maxBadI = -1
a = []
b = []
used = [False] * (n + 1)
for i in range(n):
    ta, tb = map(int, input().split())
    a.append(ta)
    b.append(tb)
    if ta >= tb and (maxGoodI == -1 or tb > b[maxGoodI]):
        maxGoodI = i
    if ta <= tb and (maxBadI == -1 or ta > a[maxBadI]):
        maxBadI = i
ans = []
maxH = 0
for i in range(n):
    if a[i] > b[i] and i != maxGoodI:
        ans.append(i + 1)
        used[i + 1] = True
        maxH += a[i] - b[i]
if maxGoodI != -1 and \
    (maxBadI != -1 and a[maxGoodI] > a[maxGoodI] - b[maxGoodI] + a[maxBadI]) or \
    (maxBadI == -1):
        maxH += a[maxGoodI]
        ans.append(maxGoodI + 1)
        used[maxGoodI + 1] = True
else:
    if maxBadI != -1:
        if maxGoodI != -1:
            maxH += a[maxGoodI] - b[maxGoodI]
            ans.append(maxGoodI + 1)
            used[maxGoodI + 1] = True
        maxH += a[maxBadI]
        if maxBadI + 1 not in ans:
            ans.append(maxBadI + 1)
        used[maxBadI + 1] = True
print(maxH)
for i in range(1, n + 1):
    if not used[i]:
        ans.append(i)
print(*ans)