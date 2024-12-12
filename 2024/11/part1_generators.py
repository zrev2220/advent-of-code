import math
import itertools

stones = list(map(int, input().strip().split()))
MAX_BLINKS = 25


def mutate(stone: int):
    stone_digits = math.floor(math.log10(stone) + 1) if stone > 0 else 1
    if stone == 0:
        yield 1
    elif stone_digits % 2 == 0:
        yield stone // 10 ** (stone_digits // 2)
        yield stone % 10 ** (stone_digits // 2)
    else:
        yield stone * 2024


for blink in range(MAX_BLINKS):
    stones = itertools.chain(*map(mutate, stones))
    stones, copy = itertools.tee(stones)
print(sum(1 for _ in stones))
