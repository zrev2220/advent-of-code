reg_a = int(input().strip().split(": ")[1])
reg_b = int(input().strip().split(": ")[1])
reg_c = int(input().strip().split(": ")[1])
input()
program = list(map(int, input().strip().split(": ")[1].split(",")))

ip = 0
output = []


def combo(operand):
    if operand <= 3:
        return operand
    if operand <= 6:
        return [reg_a, reg_b, reg_c][(operand - 1) % 3]
    raise ValueError(f"Invalid combo operand {operand}")


while ip < len(program):
    opcode, operand = program[ip : ip + 2]
    jumped = False
    if opcode == 0:
        # adv
        reg_a = reg_a // 2 ** combo(operand)
    elif opcode == 1:
        # bxl
        reg_b = reg_b ^ operand
    elif opcode == 2:
        # bst
        reg_b = combo(operand) % 8
    elif opcode == 3:
        # jnz
        if reg_a != 0:
            ip = operand
            jumped = True
    elif opcode == 4:
        # bxc
        reg_b ^= reg_c
    elif opcode == 5:
        # out
        output.append(combo(operand) % 8)
    elif opcode == 6:
        # bdv
        reg_b = reg_a // 2 ** combo(operand)
    elif opcode == 7:
        # bdv
        reg_c = reg_a // 2 ** combo(operand)

    if not jumped:
        ip += 2

print(",".join([str(n) for n in output]))
