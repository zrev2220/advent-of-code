import re

aList = []
bList = []
try:
  while True:
    a,b = map(int, re.split(' +', input().strip()))
    aList.append(a)
    bList.append(b)
except EOFError:
  pass

aList.sort()
bList.sort()
print(sum(map(lambda tup: abs(tup[0] - tup[1]), zip(aList, bList))))
