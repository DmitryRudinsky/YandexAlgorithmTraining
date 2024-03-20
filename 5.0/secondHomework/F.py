n = int(input())
listOfSectors = list(map(int, input().split()))
a, b, k = map(int, input().split())
finSector = -10 ** 9
for i in range(a, b + 1):
    currentSpeed = i
    currentNormalIndex = 0
    currentReverseIndex = 0
    while currentSpeed > 0:
        indexOfNormalList = (currentNormalIndex + 1) % n
        indexOfReverseList = (currentReverseIndex - 1) % n
        if currentSpeed > k:
            currentNormalIndex = indexOfNormalList
            currentReverseIndex = indexOfReverseList
            currentSpeed -= k
        else:
            finSector = max(finSector, listOfSectors[currentNormalIndex], listOfSectors[currentReverseIndex])
            break
print(finSector)