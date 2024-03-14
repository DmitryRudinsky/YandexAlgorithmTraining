n, k, d = map(int, input().split()) # n - к чему прибавлять, k - на что делится, d - сколько прибавлять
nowmod = n % k
ans = [n]
flag = True
for i in range(d):
    for newDigit in range(10):
        newmod = (nowmod * 10 + newDigit) % k
        if newmod == 0:
            ans.append(newDigit)
            nowmod = newmod
            break
    else:
        flag = False

if flag:
    print(''.join(map(str, ans)))
else:
    print(-1)