n = int(input())
dictLower = {}
for _ in range(n):
    s = input()
    sLower = s.lower()
    if sLower not in dictLower:
        dictLower[sLower] = set()
    dictLower[sLower].add(s)
text = input()
mistakes = 0

for word in text.split():
    wordLower = word.lower()
    if wordLower in dictLower:
        if word not in dictLower[wordLower]:
            mistakes += 1
    else:
        stresses = 0
        for c in word:
            if c.isupper():
                stresses += 1
        if stresses != 1:
            mistakes += 1
print(mistakes)