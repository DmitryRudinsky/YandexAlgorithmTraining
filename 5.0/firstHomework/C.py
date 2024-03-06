n = int(input())
res = 0
for i in range(n):
    spaceCnt = int(input())
    if spaceCnt <= 4:
        if spaceCnt == 1:
            res += 1
        elif spaceCnt == 2:
            res += 2
        elif spaceCnt == 3:
            res += 2
        elif spaceCnt == 4:
            res += 1
    else:
        fourDiv = spaceCnt % 4
        fourCnt = spaceCnt // 4
        res += fourCnt
        if fourDiv == 1:
            res += 1
        elif fourDiv == 2:
            res += 2
        elif fourDiv == 3:
            res += 2
        elif fourDiv == 4:
            res += 2
print(res)