from collections import defaultdict

rules = defaultdict(set)
total = 0


def fix(pages):
    # https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
    pages_set = set(pages)
    fixed = []

    perm_marks = set()
    temp_marks = set()
    parent = {}

    def visit(node):
        if node in perm_marks:
            return
        if node in parent:
            path = []
            next_node = node
            while next_node not in path:
                path.append(next_node)
                next_node = parent[next_node] if next_node in parent else None
            raise Exception(f"graph is cyclic: {path}")
        if node in temp_marks:
            raise Exception(f"graph is cyclic: {node}")

        temp_marks.add(node)

        for page in rules[node]:
            if page in pages_set:
                parent[node] = page
                visit(page)

        perm_marks.add(node)
        if node in pages_set:
            fixed.insert(0, node)

    while pages_set.difference(perm_marks):
        visit(list(pages_set.difference(perm_marks))[0])

    return fixed


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
            valid = True
            processed = set()
            for page in pages:
                if processed.intersection(rules[page]):
                    valid = False
                    break
                processed.add(page)
            if not valid:
                fixed = fix(pages)
                mid = fixed[len(fixed) // 2]
                total += mid
except EOFError:
    pass

print(total)
