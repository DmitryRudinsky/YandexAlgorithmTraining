field = [list("-" * 10)]
for i in range(8):
    field.append(["-"] + list(input()) + ["-"])
field.append(list("-" * 10))
for i in range(10):
    for j in range(10):
        if field[i][j] == "R" or field[i][j] == "B":
            if field[i][j] == "R":
                di = [1, -1, 0, 0]
                dj = [0, 0, 1, -1]
            elif field[i][j] == "B":
                di = [1, -1, 1, -1]
                dj = [1, 1, -1, -1]
            for dir in range(4):
                ni, nj = i + di[dir], j + dj[dir]
                while field[ni][nj] == "*" or field[ni][nj] == ".":
                    field[ni][nj] = "."
                    ni += di[dir]
                    nj += dj[dir]
ans = 0
for row in field:
    for cells in row:
        if cells == "*":
            ans += 1
print(ans)