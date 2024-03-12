n = int(input())
current = 0
output = []

numbers = list(map(lambda x: abs(int(x)) % 10, input().split()))
current = numbers[0]

for _ in range(1, n):
    temp = numbers[_]
    if temp % 2 == 0:
        current += temp
        output.append('+')
    else:
        if current % 2 == 0:
            current += temp
            output.append('+')
        else:
            current *= temp
            output.append('x')

print(''.join(output))
