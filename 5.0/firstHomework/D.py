chessArr = []
placesArr = []
BArr = []
RArr = []
beatPlaces = 0
for i in range(0, 8):
    line = str(input())
    chessArr.append(line)
    if line.find("R") != -1 or line.find("B") != -1:
        for j in range(len(line)):
            if line[j] == "R":
                RArr.append((i, j))
            elif line[j] == "B":
                BArr.append((i, j))

for elem in BArr:
    if elem not in placesArr:
        placesArr.append(elem)
        beatPlaces += 1
    stroka = elem[0]
    stolbec = elem[1]
    while stroka >= 1 and stolbec >= 1:
        if chessArr[stroka - 1][stolbec - 1] == "*":
            if (stroka - 1, stolbec - 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka - 1, stolbec - 1))
                stroka = stroka - 1
                stolbec = stolbec - 1
            elif (stroka - 1, stolbec - 1) in placesArr and (stroka - 2, stolbec - 2) not in placesArr:
                stroka = stroka - 1
                stolbec = stolbec - 1
            elif (stroka - 1, stolbec - 1) in placesArr and (stroka - 2, stolbec - 2) in placesArr:
                stroka = stroka - 2
                stolbec = stolbec - 2
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stroka <= 6 and stolbec <= 6:
        if chessArr[stroka + 1][stolbec + 1] == "*":
            if (stroka + 1, stolbec + 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka + 1, stolbec + 1))
                stroka = stroka + 1
                stolbec = stolbec + 1
            elif (stroka + 1, stolbec + 1) in placesArr and (stroka + 2, stolbec + 2) not in placesArr:
                stroka = stroka + 1
                stolbec = stolbec + 1
            elif (stroka + 1, stolbec + 1) in placesArr and (stroka + 2, stolbec + 2) in placesArr:
                stroka = stroka + 2
                stolbec = stolbec + 2
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stroka >= 1 and stolbec <= 6:
        if chessArr[stroka - 1][stolbec + 1] == "*":
            if (stroka - 1, stolbec + 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka - 1, stolbec + 1))
                stroka = stroka - 1
                stolbec = stolbec + 1
            elif (stroka - 1, stolbec + 1) in placesArr and (stroka - 2, stolbec + 2) not in placesArr:
                stroka = stroka - 1
                stolbec = stolbec + 1
            elif (stroka - 1, stolbec + 1) in placesArr and (stroka - 2, stolbec + 2) in placesArr:
                stroka = stroka - 2
                stolbec = stolbec + 2
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stroka <= 6 and stolbec >= 1:
        if chessArr[stroka + 1][stolbec - 1] == "*" :
            if (stroka + 1, stolbec - 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka + 1, stolbec - 1))
                stroka = stroka + 1
                stolbec = stolbec - 1
            elif (stroka + 1, stolbec - 1) in placesArr and (stroka + 2, stolbec - 2) not in placesArr:
                stroka = stroka + 1
                stolbec = stolbec - 1
            elif (stroka + 1, stolbec - 1) in placesArr and (stroka + 2, stolbec - 2) in placesArr:
                stroka = stroka + 2
                stolbec = stolbec - 2
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]

for elem in RArr:
    if elem not in placesArr:
        placesArr.append(elem)
        beatPlaces += 1
    stroka = elem[0]
    stolbec = elem[1]
    while stroka >= 1:
        if chessArr[stroka - 1][stolbec] == "*":
            if (stroka - 1, stolbec) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka - 1, stolbec))
                stroka = stroka - 1
            elif (stroka - 1, stolbec) in placesArr and (stroka - 2, stolbec) not in placesArr:
                stroka = stroka - 1
            elif (stroka - 1, stolbec) in placesArr and (stroka - 2, stolbec) in placesArr and chessArr[stroka - 2][stolbec] == "*":
                stroka = stroka - 2
            elif (stroka - 1, stolbec) in placesArr and (stroka - 2, stolbec) in placesArr and chessArr[stroka - 2][stolbec] != "*":
                stroka = stroka - 8
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stroka <= 6:
        if chessArr[stroka + 1][stolbec] == "*":
            if (stroka + 1, stolbec) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka + 1, stolbec))
                stroka = stroka + 1
            elif (stroka + 1, stolbec) in placesArr and (stroka + 2, stolbec) not in placesArr:
                stroka = stroka + 1
            elif (stroka + 1, stolbec) in placesArr and (stroka + 2, stolbec) in placesArr and chessArr[stroka + 2][stolbec] == "*":
                stroka = stroka + 2
            elif (stroka + 1, stolbec) in placesArr and (stroka + 2, stolbec) in placesArr and chessArr[stroka + 2][stolbec] != "*":
                stroka = stroka + 8
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stolbec <= 6:
        if chessArr[stroka][stolbec + 1] == "*":
            if (stroka, stolbec + 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka, stolbec + 1))
                stolbec = stolbec + 1
            elif (stroka, stolbec + 1) in placesArr and (stroka, stolbec + 2) not in placesArr:
                stolbec = stolbec + 1
            elif (stroka, stolbec + 1) in placesArr and (stroka, stolbec + 2) in placesArr and chessArr[stroka][stolbec + 2] == "*":
                stolbec = stolbec + 2
            elif (stroka, stolbec + 1) in placesArr and (stroka, stolbec + 2) in placesArr and chessArr[stroka][stolbec + 2] != "*":
                stolbec = stolbec + 8

        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
    while stolbec >= 1:
        if chessArr[stroka][stolbec - 1] == "*":
            if (stroka, stolbec - 1) not in placesArr:
                beatPlaces += 1
                placesArr.append((stroka, stolbec - 1))
                stolbec = stolbec - 1
            elif (stroka, stolbec - 1) in placesArr and (stroka, stolbec - 2) not in placesArr:
                stolbec = stolbec - 1
            elif (stroka, stolbec - 1) in placesArr and (stroka, stolbec - 2) in placesArr and chessArr[stroka][stolbec - 2] == "*":
                stolbec = stolbec - 2
            elif (stroka, stolbec - 1) in placesArr and (stroka, stolbec - 2) in placesArr and chessArr[stroka][stolbec - 2] != "*":
                stolbec = stolbec - 8
        else:
            break
    stroka = elem[0]
    stolbec = elem[1]
print(64 - beatPlaces)