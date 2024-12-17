import re
from decimal import Decimal
import decimal

# decimal.getcontext().prec = 6

A_COST = 3
B_COST = 1
EPSILON = Decimal(0.0001)
round = lambda n: int(n + 0.5)

first = True
total = Decimal(0)
try:
    while True:
        if first:
            first = False
        else:
            input()
        ax, ay = map(
            Decimal, re.match(r"Button A: X\+(\d+), Y\+(\d+)", input().strip()).groups()
        )
        bx, by = map(
            Decimal, re.match(r"Button B: X\+(\d+), Y\+(\d+)", input().strip()).groups()
        )
        prize_x, prize_y = map(
            lambda n: Decimal(n) + 10000000000000,
            re.match(r"Prize: X=(\d+), Y=(\d+)", input().strip()).groups(),
        )

        N = 2
        matrix = [
            [ax, bx, prize_x],
            [ay, by, prize_y],
        ]
        print("-----------")
        print(*[" ".join(map(str, row)) for row in matrix], sep="\n")

        # forward elimination
        i = 0
        j = 1
        ratio = matrix[j][i] / matrix[i][i]
        for k in range(N + 1):
            matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

        # back substitution
        ans_b: Decimal = matrix[N - 1][N] / matrix[N - 1][N - 1]
        ans_a: Decimal = matrix[i][N]
        ans_a = ans_a - matrix[i][j] * ans_b
        ans_a = ans_a / matrix[i][i]

        print(ans_a, ans_a.as_integer_ratio())
        print(ans_b, ans_a.as_integer_ratio())
        # reject decimal solutions (can't press a button 0.3 times)
        if (
            abs(ans_a - ans_a.to_integral_value()) > EPSILON
            or abs(ans_b - ans_b.to_integral_value()) > EPSILON
        ):
            print("impossible")
            continue
        total += ans_a * A_COST + ans_b * B_COST

except EOFError:
    pass
print(total.to_integral_value())
