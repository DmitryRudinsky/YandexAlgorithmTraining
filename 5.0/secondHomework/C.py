n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
mxNum = numbers.pop()
sumNum = sum(numbers)
if mxNum > sumNum:
    print(mxNum - sumNum)
else:
    print(mxNum + sumNum)