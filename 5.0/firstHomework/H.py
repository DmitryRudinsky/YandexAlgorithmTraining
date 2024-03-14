l, x1, v1, x2, v2 = map(int, input().split())
ans = 10 ** 30


for rotation in range(2):
    deltax = (x2 - x1 + l) % l
    deltav = v1 - v2
    if deltav < 0:
        deltav = -deltav
        deltax = (-deltax + l) % l
    if deltax == 0:
        ans = 0
    if deltav != 0:
        ans = min(ans, deltax / deltav)
    x2 = (-x2 + l) % l
    v2 = -v2
if ans == 10 ** 30:
    print("NO")
else:
    print("YES")
    print(ans)