P, V = (map(int, input().split()))
Q, M = (map(int, input().split()))
vasya_start, vasya_end = P - V, P + V
masha_start, masha_end = Q - M, Q + M
if max(vasya_start, masha_start) <= min(vasya_end, masha_end):
    print(max(vasya_end, masha_end) - min(vasya_start, masha_start) + 1)
else:
    print((vasya_end - vasya_start + 1) + (masha_end - masha_start + 1))