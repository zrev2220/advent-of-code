from collections import defaultdict

nodes = set()
adj = defaultdict(set)
try:
    while True:
        a, b = input().strip().split("-")
        nodes.update((a, b))
        adj[a].add(b)
        adj[b].add(a)
except EOFError:
    pass

# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
cliques = []


def bron_kerbosch(R, P, X):
    if not P and not X:
        cliques.append(R)
    else:
        while P:
            v = next(iter(P))
            bron_kerbosch(R | {v}, P & adj[v], X & adj[v])
            P.remove(v)
            X.add(v)


bron_kerbosch(set(), nodes, set())
print(",".join(sorted(max(cliques, key=lambda c: len(c)))))
