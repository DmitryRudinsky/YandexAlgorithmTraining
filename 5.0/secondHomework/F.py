n = int(input())
listOfSectors = list(map(int, input().split()))
listOfSectorsRev = [listOfSectors[0]] + listOfSectors[-1:0:-1]
a, b, k = map(int, input().split())
finSector = -10 ** 9
for i in range(a, b + 1):
    currentSpeed = i + k
    currentNormalSector = listOfSectors[0]
    currentReverseSector = listOfSectorsRev[0]
    j = 0
    while currentSpeed > 0:
        elemOfNormalList = listOfSectors[j]
        elemOfReverseList = listOfSectorsRev[j]
        j = (j + 1) % n
        if currentSpeed > k:
            currentNormalSector = elemOfNormalList
            currentReverseSector = elemOfReverseList
            currentSpeed -= k
            print(currentSpeed, currentNormalSector, currentReverseSector)
        else:
            finSector = max(finSector, currentNormalSector, currentReverseSector)
            break
print(finSector)