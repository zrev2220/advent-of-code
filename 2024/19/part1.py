from functools import cache

towels = input().strip().split(", ")
input()


@cache
def make_pattern(pattern: str) -> bool:
    if pattern in towels:
        return True
    possible = False
    for towel in towels:
        if pattern.startswith(towel):
            possible = make_pattern(pattern[len(towel) :]) or possible
    return possible


possible = 0
try:
    while True:
        if make_pattern(input().strip()):
            possible += 1
except EOFError:
    pass
print(possible)
