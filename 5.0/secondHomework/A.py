n = int(input())
xArr = []
yArr = []
for i in range(n):
    coord = list(map(int, input().split()))
    xArr.append(coord[0])
    yArr.append(coord[1])
print(min(xArr), min(yArr), max(xArr), max(yArr))