import sys


def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    crate_stacks = {}
    parsing_crates = True

    for row, l in enumerate(lines):
        if l == '\n' or l.replace(' ', '').replace('\n', '').isdecimal():
            parsing_crates = False
            print('Parsed crate:', crate_stacks)
            continue

        if parsing_crates:
            for col, c in enumerate(l):
                if (col - 1) % 4 == 0:
                    crate_index = int((col - 1) / 4)

                    try:
                        if c != ' ':
                            crate_stacks[crate_index].insert(0, c)
                    except:
                        crate_stacks[crate_index] = [c]
        else:
            parsed_instruction = l.split(' ')
            move_count: int = int(parsed_instruction[1])
            from_index: int = int(parsed_instruction[3]) - 1
            to_index: int = int(parsed_instruction[5]) - 1
            print(crate_stacks)

            for _ in range(move_count - 1):
                crate_stacks[to_index].extend(crate_stacks[from_index].pop())

    print(''.join(v[-1] for k, v in crate_stacks.items()))

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
