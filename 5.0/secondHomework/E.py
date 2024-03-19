n = int(input())
listOfBerries = []
currentHeight = 0
maxHeight = 0
for i in range(n):
    up, down = (map(int, input().split()))
    listOfBerries.append((up, down, i + 1))
listOfBerriesSorted = sorted(listOfBerries, key=lambda x: (-x[0], x[1]))
print(listOfBerriesSorted)
listOfBerries.clear()
for paar in listOfBerriesSorted:
    up, down, num = paar
    currentHeight += up
    maxHeight = max(maxHeight, currentHeight)
    currentHeight -= down
    listOfBerries.append(num)
print(maxHeight)
print(' '.join(map(str, listOfBerries)))