from functools import cache


@cache
def mix(a, b):
    return a ^ b


@cache
def prune(n):
    return n % 16777216


@cache
def next_secret(n):
    a = n * 64
    n = mix(a, n)
    n = prune(n)

    b = n // 32
    n = mix(b, n)
    n = prune(n)

    c = n * 2048
    n = mix(c, n)
    n = prune(n)

    return n


N = 2000
try:
    while True:
        n = int(input().strip())
        prices = [n % 10]
        for _ in range(N):
            n = next_secret(n)
            prices.append(n % 10)
        print(''.join(map(str, prices)))
except EOFError:
    pass
