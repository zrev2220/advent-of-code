from collections import defaultdict
from itertools import combinations

edges = set()
nodes = set()
adj = defaultdict(set)
try:
    while True:
        a, b = input().strip().split("-")
        nodes.update((a, b))
        edges.add(tuple(sorted((a, b))))
        adj[a].add(b)
        adj[b].add(a)
except EOFError:
    pass

triplets = set()
visited = set()

for node in nodes:
    neighbors = sorted(adj[node])
    for pair in combinations(
        filter(lambda n: node.startswith("t") or n.startswith("t"), neighbors), 2
    ):
        if pair in edges:
            triplets.add(tuple(sorted((node, *pair))))
    visited.add(node)
print(len(triplets))
