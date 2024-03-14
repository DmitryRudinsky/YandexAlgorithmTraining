n = int(input())
numbers = list(map(int, input().split()))
state = "no odd"
ans = []
for num in numbers:
    if state == "no odd":
        if num % 2 == 0:
            ans.append("+")
        else:
            state = "last odd"
    elif state == "last odd":
        if num % 2 == 0:
            ans.append("+")
            state = "all even"
        else:
            ans.append("x")
    elif state == "all even":
        ans.append("x")


print("".join(ans))