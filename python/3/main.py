import sys

PRIORITIES = {
    **{letter: ord(letter) - 96 for letter in map(chr, range(97, 123))},
    **{letter: ord(letter) - 38 for letter in map(chr, range(65, 91))},
}

def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    priorities_sum = 0
    for l in lines:
        items = dict()
        for i, c in enumerate(l):
            if i < len(l) / 2:
               items[c] = 1
            else:
                if items.get(c, None):
                    priorities_sum += PRIORITIES[c]

    print(priorities_sum)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
