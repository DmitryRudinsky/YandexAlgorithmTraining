def twoterms(nums, x):
    prevNums = set()
    for nowNum in nums:
        if x - nowNum in prevNums:
            return nowNum, x - nowNum
        prevNums.add(nowNum)
    return 0, 0


nums = (3, 2, 4, 1, 7)
print(twoterms(nums, 9))
