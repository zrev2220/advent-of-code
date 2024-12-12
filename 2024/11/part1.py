stones = list(map(int, input().strip().split()))
MAX_BLINKS = 25
for blink in range(MAX_BLINKS):
    new_stones = []
    for stone in stones:
        str_stone = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(str_stone) % 2 == 0:
            halfway = len(str_stone) // 2
            new_stones.extend(map(int, [str_stone[:halfway], str_stone[halfway:]]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
print(len(stones))
