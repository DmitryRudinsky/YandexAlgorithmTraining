def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)


n, k, d = map(int, input().split()) # n - к чему прибавлять, k - на что делится, d - сколько прибавлять

if k == 0 or n == 0 or d == 0:
    print(-1)
else:
    for i in range(d):
        flag = False
        for j in range(10):
            if (n * 10 + j) % k == 0:
                n = n * 10 + j
                flag = True
                break
        if flag:
            continue
        else:
            n = -1
            break
    print(n)