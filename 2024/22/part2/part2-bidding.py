from collections import defaultdict

from tqdm import tqdm

trends = defaultdict(lambda: defaultdict(int))
i = 1
try:
    while True:
        print(f"\rprocessing {i}", end="")
        prices = map(int, input().strip())
        last = None
        history = tuple()
        placed = set()
        for p in prices:
            if last is not None:
                diff = p - last
                history = (*history, diff)[-4::]
            if len(history) == 4 and history not in placed:
                trends[history][p] += 1
                placed.add(history)
            elif len(history) > 4:
                raise RuntimeError(f"{len(history)=}")
            last = p
        i += 1
except EOFError:
    pass

print("\nfinishing")
best = None
for history, prices in trends.items():
    total = sum(price * freq for price, freq in prices.items())
    possible = (total, history)
    if best is None or possible > best:
        best = possible
print(best)
