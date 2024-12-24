import re


leaves = {}
gates = {}
reading_initials = True
try:
    while True:
        line = input().strip()
        if line:
            if reading_initials:
                wire, raw_value = re.match(r"(.+): (0|1)", line).groups()
                value = int(raw_value) == 1
                leaves[wire] = value
            else:
                a, gate, b, c = re.match(
                    r"(.+) (AND|OR|XOR) (.+) -> (.+)", line
                ).groups()
                gates[c] = (gate, a, b)
        else:
            reading_initials = False
except EOFError:
    pass


def resolve(wire: str) -> bool:
    if wire in leaves:
        return leaves[wire]
    gate, a, b = gates[wire]
    a_value = resolve(a)
    b_value = resolve(b)
    if gate == "AND":
        return a_value and b_value
    elif gate == "OR":
        return a_value or b_value
    else:
        return a_value != b_value


result = 0
for wire in (wire for wire in gates if wire.startswith("z")):
    if r := resolve(wire):
        result += 2 ** int(wire[1:])
print(result)
