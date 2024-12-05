from collections import defaultdict

rules = defaultdict(set)
total = 0

try:
    is_reading_rules = True
    while True:
        line = input().strip()
        if line == "":
            is_reading_rules = False
        elif is_reading_rules:
            x, y = map(int, line.split("|"))
            rules[x].add(y)
        else:
            pages = [int(n) for n in line.split(",")]
            mid = pages[len(pages) // 2]
            valid = True
            processed = set()
            for page in pages:
                if processed.intersection(rules[page]):
                    valid = False
                    break
                processed.add(page)
            if valid:
                total += mid
except EOFError:
    pass

print(total)
