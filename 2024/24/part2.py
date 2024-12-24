# nothing here explicitly solves part 2
# I used this to manually debug which wires were wired up incorrectly

from collections import defaultdict
import re
import traceback


leaves = {}
gates = {}

wires = defaultdict(list)

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
                wires[a].append((c, gate))
                wires[b].append((c, gate))
        else:
            reading_initials = False
except EOFError:
    pass


x = 0
y = 0
for leaf, value in leaves.items():
    if leaf.startswith("x") and value:
        x += 2 ** int(leaf[1:])
    elif leaf.startswith("y") and value:
        y += 2 ** int(leaf[1:])
true_result = x + y
print(f"{x} + {y} = {true_result}")


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
print(
    "  "
    + "".join(
        [
            f"{bit // 10 if bit % 10 == 0 else ' '}"
            for bit in range(len(bin(result)[2:]))
        ][::-1]
    )
)
print("  " + "".join([f"{bit % 10}" for bit in range(len(bin(result)[2:]))][::-1]))
print(bin(result))
print(bin(true_result))

wrong = []
for i in range(len(bin(result)[2:])):
    result_bit = result & (1 << i)
    true_bit = true_result & (1 << i)
    if result_bit != true_bit:
        print(f"bit {i} is wrong")
        wrong.append(i)


def make_mermaid(wire):
    if wire in leaves:
        return f"{wire}([{int(leaves[wire])}])"
    else:
        gate, a, b = gates[wire]
        return f"""{wire}_{gate}({gate})
    {wire}_{gate}--"{a}"-->{make_mermaid(a)}
    {wire}_{gate}--"{b}"-->{make_mermaid(b)}"""


for bit in wrong + [1]:
    wire = f"z{bit:02}"

    gate, _, __ = gates[wire]
    if gate != "XOR":
        print(f"{wire} is not tied to an XOR ({gate})")

    # with open(f"mermaid/{wire}.txt", "w") as f:
    #     print("flowchart TD", file=f)
    #     print(
    #         f'    {wire}@{{ shape: sm-circ }}--"{wire}"-->{make_mermaid(wire)}', file=f
    #     )


def print_wire(wire, name=""):
    print(f"{name} {wire=} wires={wires[wire]} gates={gates.get(wire, None)}")


carry = None
for bit in range(len(bin(result)[2:])):
    print(f"Checking bit {bit:02}")
    x = f"x{bit:02}"
    y = f"y{bit:02}"
    z = f"z{bit:02}"

    try:
        print(f"{carry=}")
        if carry is None:
            xor_gate = next(wire for wire, gate in wires[x] if gate == "XOR")
            assert [
                wire for wire, gate in wires[y] if gate == "XOR" and wire == xor_gate
            ]
            assert xor_gate == z
            carry = next(wire for wire, gate in wires[x] if gate == "AND")
        else:
            xor_gate1 = next(wire for wire, gate in wires[x] if gate == "XOR")
            assert [
                wire for wire, gate in wires[y] if gate == "XOR" and wire == xor_gate1
            ]
            xor_gate2 = next(wire for wire, gate in wires[xor_gate1] if gate == "XOR")
            assert [
                wire
                for wire, gate in wires[carry]
                if gate == "XOR" and wire == xor_gate2
            ]
            assert xor_gate2 == z

            and_gate1 = next(wire for wire, gate in wires[x] if gate == "AND")
            assert [
                wire for wire, gate in wires[y] if gate == "AND" and wire == and_gate1
            ]
            and_gate2 = next(wire for wire, gate in wires[carry] if gate == "AND")
            assert [
                wire
                for wire, gate in wires[xor_gate1]
                if gate == "AND" and wire == and_gate2
            ]
            assert len(wires[and_gate1]) == 1
            assert len(wires[and_gate2]) == 1
            carry, _ = wires[and_gate1][0]
    except (AssertionError, StopIteration) as e:
        print()
        traceback.print_exc()
        print_wire(x)
        print_wire(y)
        print_wire(z)
        print_wire(carry, "carry")
        print(f"{z} gates")
        _, a, b = gates[z]
        print_wire(a)
        print_wire(b)
        print()
        print_wire(xor_gate1, "xor_gate1")
        print_wire(xor_gate2, "xor_gate2")
        break

# nwq,z36,z18,fvw,wpq,grf,mdb,z22
# ↓
# fvw,grf,mdb,nwq,wpq,z18,z22,z36
