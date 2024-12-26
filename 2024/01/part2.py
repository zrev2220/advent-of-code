import re
from collections import Counter

aList = []
bCounter = Counter()
try:
    while True:
        a, b = map(int, re.split(" +", input().strip()))
        aList.append(a)
        bCounter[b] += 1
except EOFError:
    pass

score = 0
for a in aList:
    score += a * bCounter[a]
print(score)
