n_safe = 0


def get_report_options(report):
    yield report
    for i in range(len(report)):
        yield report[:i] + report[i + 1 :]


try:
    while True:
        report = list(map(int, input().strip().split()))
        for report_option in get_report_options(report):
            safe = True

            prevdiff = None
            for i in range(1, len(report_option)):
                prev = report_option[i - 1]
                level = report_option[i]
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
                break
except EOFError:
    pass

print(n_safe)
