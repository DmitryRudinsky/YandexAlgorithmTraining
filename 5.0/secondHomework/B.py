N, K = (map(int, input().split()))
prises = list(map(int, input().split()))
mx = 0
for i in range(N):
    start = prises[i]
    for j in range(i + 1, i + K + 1):
        if j <= len(prises) - 1:
            mx = max(mx, prises[j] - start)
print(mx)