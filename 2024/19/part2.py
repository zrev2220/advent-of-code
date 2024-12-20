from functools import cache

towels = input().strip().split(", ")
input()


@cache
def make_pattern(pattern: str) -> int:
    if len(pattern) == 0:
        return 1
    result = 0
    for towel in towels:
        if pattern.startswith(towel):
            result += make_pattern(pattern[len(towel) :])
    return result


result = 0
try:
    while True:
        result += make_pattern(input().strip())
except EOFError:
    pass
print(result)
