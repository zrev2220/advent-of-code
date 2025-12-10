import itertools
import multiprocessing
import sys

from sympy.matrices import Matrix
from tqdm import tqdm
import z3

ans = 0


def get_chunks(size):
    while True:
        chunk = itertools.islice(lines, size)
        if chunk is None:
            break
        yield chunk


def process_combinations_chunk(args):
    combinations_chunk, arref_data, free_vars, num_buttons, max_joltage = args

    id = multiprocessing.current_process()._identity[0] % multiprocessing.cpu_count()

    x = z3.Ints(" ".join([f"x{i}" for i in range(num_buttons)]))
    s = z3.Solver()
    s.add(xi >= 0 for xi in x)

    m = arref_data.shape[0]
    for i in range(m):
        row = arref_data.row(i)
        cells, rhs = row[:-1], row[-1]
        lhs = sum(
            (z3.Q(c.p, c.q) if c.is_rational else c) * xi
            for c, xi in zip(cells, x)
            if c != 0
        )
        s.add(lhs == rhs)

    best = None
    for combination in tqdm(
        combinations_chunk,
        position=id + 1,
        desc=f"CPU{id:02}",
        leave=False,
    ):
        s.push()
        for i, free_i in enumerate(free_vars):
            s.add(x[free_i] == combination[i])

        if s.check() == z3.sat:
            model = s.model()
            total = sum([model[var].as_long() for var in x])
            best = min(best, total) if best is not None else total

        s.pop()

    return best


if __name__ == "__main__":
    lines = list(sys.stdin)
    cpus = multiprocessing.cpu_count()
    chunk_size = max(1, len(lines) // cpus)

    for line in tqdm(lines, position=0, desc="Lines"):
        if not line:
            break
        parts = line.split()
        buttonsStr = parts[1:-1]
        joltageStr = parts[-1]

        buttons = [list(map(int, item[1:-1].split(","))) for item in buttonsStr]
        joltage = list(map(int, joltageStr[1:-1].split(",")))
        maxJoltage = max(joltage)

        m = len(joltage)
        n = len(buttons) + 1
        A = Matrix(m, n, lambda _, __: 0)
        for i, jolt in enumerate(joltage):
            A[i, n - 1] = jolt
        for j, button in enumerate(buttons):
            for wire in button:
                A[wire, j] = 1

        Arref, pivots = A.rref()
        free_vars = [i for i in range(len(buttons)) if i not in pivots]

        all_combinations = list(
            itertools.product(range(maxJoltage + 1), repeat=len(free_vars))
        )
        total_combinations = len(all_combinations)

        chunk_size = max(1, total_combinations // cpus)
        chunks = [
            all_combinations[i : i + chunk_size]
            for i in range(0, total_combinations, chunk_size)
        ]

        with multiprocessing.Pool(processes=cpus) as pool:
            results = pool.map(
                process_combinations_chunk,
                [
                    (chunk, Arref, free_vars, len(buttons), maxJoltage)
                    for chunk in chunks
                ],
            )

        best = min(result for result in results if result is not None)
        ans += best

    print(ans)
