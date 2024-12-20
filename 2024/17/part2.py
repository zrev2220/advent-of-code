# got hints from various comments here:
# https://www.reddit.com/r/adventofcode/comments/1hg69ql/2024_day_17_part_2_can_someone_please_provide_a/
# https://www.reddit.com/r/adventofcode/comments/1hgcuw8/2024_day_17_part_2_any_hints_folks/
# https://www.reddit.com/r/adventofcode/comments/1hhtc6g/2024_day_17_part_2_explanation_of_the_solution/

ANS = (2,4,1,3,7,5,0,3,4,3,1,5,5,5,3,0)


def the_program(a):
    """
    The input program, translated to Python
    """

    og_a = a

    output = []

    while a != 0:
        # --- 1-1 translation ---
        # b = a % 8
        # b ^= 3
        # c = a // 2**b
        # a //= 2**3  # a //= 8
        # b ^= c
        # b ^= 5

        # --- simplified ---
        b = (a % 8) ^ 3
        c = a // 2**b
        b ^= c ^ 5
        a //= 2**3  # a //= 8

        output.append(b % 8)

    tup_output = tuple(output)
    if tup_output == ANS:
        print(output, f"{og_a} / {hex(og_a)}")
        print(ANS)
        print("🎉💥🎆💥🎉")
        exit()
    return tup_output


def search(*, a, depth):
    if depth > len(ANS):
        return

    indent = " " * depth
    print(indent, f"🔎 search({a=} / {hex(a)}, {depth=})")
    for i in range(8):
        new_a = (a << 3) + i
        output = the_program(new_a)
        print(indent, output, f"a={new_a} / {hex(new_a)}")
        if output[-(depth + 1) :] == ANS[-(depth + 1) :]:
            search(a=new_a, depth=depth + 1)


print(ANS)
search(a=0, depth=0)
print("search failed 😢")
exit(1)
