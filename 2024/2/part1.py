n_safe = 0

try:
    while True:
        report = list(map(int, input().strip().split()))
        safe = True
        prevdiff = None
        for i in range(1, len(report)):
            prev = report[i-1]
            level = report[i]
            diff = level - prev
            if abs(diff) > 3 or diff == 0:
                safe = False
                break
            if prevdiff is None:
                prevdiff = diff
                continue
            if (prevdiff <= 0) != (diff <= 0):
                safe = False
                break

        if safe:
            n_safe += 1
except EOFError:
    pass

print(n_safe)
