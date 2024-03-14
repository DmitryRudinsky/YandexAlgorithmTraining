def calc(t, myUnits, barHp, enemyProad):
    rounds = 0
    enemyUnits = 0
    while barHp >= t:
        if enemyUnits >= myUnits:
            return 10 ** 9
        barHp -= myUnits - enemyUnits
        enemyUnits = 0
        if barHp >= 0:
            enemyUnits += enemyProad
        rounds += 1
    while barHp > 0:
        if myUnits <= 0:
            return 10 ** 9
        if barHp >= myUnits:
            barHp -= myUnits
        else:
            enemyUnits -= myUnits - barHp
            barHp = 0
        myUnits -= enemyUnits
        if barHp > 0:
            enemyUnits += enemyProad
        rounds += 1
    while enemyUnits > 0:
        if myUnits <= 0:
            return 10 ** 9
        enemyUnits -= myUnits
        if enemyUnits > 0:
            myUnits -= enemyUnits
        rounds += 1
    return rounds


x = int(input())
y = int(input())
p = int(input())
ans = 10 ** 9

for t in range(0, y + 1):
    ans = min(ans, calc(t, x, y, p))
if ans != 10 ** 9:
    print(ans)
else:
    print(-1)