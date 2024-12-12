import math
from collections import defaultdict

stones = list(map(int, input().strip().split()))
MAX_BLINKS = 75

memo = defaultdict(dict)


def observe(stone: int, depth: int) -> int:
    if stone in memo and depth in memo[stone]:
        return memo[stone][depth]
    if depth == MAX_BLINKS:
        return 1

    stone_digits = math.floor(math.log10(stone) + 1) if stone > 0 else 1
    if stone == 0:
        result = observe(1, depth + 1)
    elif stone_digits % 2 == 0:
        result = observe(stone // 10 ** (stone_digits // 2), depth + 1) + observe(
            stone % 10 ** (stone_digits // 2), depth + 1
        )
    else:
        result = observe(stone * 2024, depth + 1)
    memo[stone][depth] = result
    return result


print(sum(observe(stone, 0) for stone in stones))
