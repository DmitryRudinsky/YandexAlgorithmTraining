Vasya = list(map(int, input().split()))
Masha = list(map(int, input().split()))
P, V, Q, M = Vasya[0], Vasya[1], Masha[0], Masha[1]
if(P > Q):
    P, Q = Q, P
vasya_start = P - V
vasya_end = P + V
masha_start = Q - M
masha_end = Q + M
#print(vasya_start, vasya_end, masha_start, masha_end)
res = 0
if vasya_end < masha_start:
    res += len(range(vasya_start, vasya_end + 1)) + len(range(masha_start, masha_end + 1))
elif vasya_end > masha_start and vasya_start < masha_start and vasya_end < masha_end:
    res += len(range(vasya_start, masha_start + 1)) + len(range(masha_start + 1, masha_end + 1))
elif(masha_start > vasya_start and masha_end < vasya_end):
    res += len(range(vasya_start, vasya_end + 1))
elif(masha_start < vasya_start and masha_end > vasya_end):
    res += len(range(masha_start, masha_end + 1))
else:
    res += len(range(vasya_start, masha_end + 1))
print(res)