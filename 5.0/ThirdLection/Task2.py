mods = [10 ** 9 + 7, 10 ** 9 + 11, 10 ** 9 + 13]
maxfibnum = 40000
usedhashes = []
for _ in range(len(mods)):
    usedhashes.append(set())
for i in range(len(mods)):
    f1 = 1
    f2 = 1
    usedhashes[i].add(1)
    for j in range(maxfibnum):
        f1, f2 = f2, (f1 + f2) % mods[i]
        usedhashes[i].add(f2)

ans = []
n = int(input())
for i in range(n):
    now = int(input())
    isFib = True
    for j in range(len(mods)):
        isFib = isFib and now % mods[i] in usedhashes[i]
    if isFib:
        ans.append("YES")
    else:
        ans.append("NO")
print('\n'.join(ans))

