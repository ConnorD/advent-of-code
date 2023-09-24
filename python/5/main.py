import sys


def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    crate_stacks = {}
    parsing_crates = True

    for row, l in enumerate(lines):
        if l == '\n' or l.replace(' ', '').replace('\n', '').isdecimal():
            parsing_crates = False
            continue

        if parsing_crates:
            for col, c in enumerate(l):
                if (col - 1) % 4 == 0:
                    crate_index = int((col - 1) / 4)

                    try:
                        if c != ' ':
                            crate_stacks[crate_index].append(c)
                    except:
                        crate_stacks[crate_index] = [c]
        else:
            parsed_instruction = l.split(' ')
            move_count: int = int(parsed_instruction[1])
            from_index: int = int(parsed_instruction[3]) - 1
            to_index: int = int(parsed_instruction[5]) - 1
            print(move_count, from_index, to_index)
            for _ in range(move_count - 1):
                crate_stacks[to_index].append(crate_stacks[from_index].pop())

    print(crate_stacks)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
