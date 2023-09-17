import sys

PRIORITIES = {
    **{letter: ord(letter) - 96 for letter in map(chr, range(97, 123))},
    **{letter: ord(letter) - 38 for letter in map(chr, range(65, 91))},
}

def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    priorities_sum = 0
    group_chars = dict()

    for line_number, l in enumerate(lines):
        for i, c in enumerate(l):
            if group_chars.get(c, (-1, 0))[0] != line_number % 3:
                group_chars[c] = (line_number % 3, group_chars.get(c, (None, 0))[1] + 1)

            if line_number > 0 and (line_number + 1) % 3 == 0 and group_chars[c][1] == 3:
                print(f'group badge: {c}')
                priorities_sum += PRIORITIES[c]
                group_chars = dict()
                break

    print(priorities_sum)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
