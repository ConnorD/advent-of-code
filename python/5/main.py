import sys


def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    crate_stacks = []
    parsing_crates = True

    for row, l in enumerate(lines):
        if l == '\n':
            parsing_crates = False

        for col, c in enumerate(l):
            if c.isdecimal():
                parsing_crates = False
                continue

            if parsing_crates:
                if (col - 1) % 4 == 0:
                    crate_index = int((col - 1) / 4)
                    try:
                        crate_stacks[crate_index].append(c)
                    except:
                        crate_stacks.append([c])
            else:
                pass

    print(crate_stacks)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
