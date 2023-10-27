import sys

NUM_DISTINCT_CHARACTERS = 14

def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    for i, l in enumerate(lines):
        if l == '\n':
            break
        
        for c in range(0, len(l)):
            current_substr = l[c:c + NUM_DISTINCT_CHARACTERS]
            if len(set(current_substr)) == len(current_substr):
                print(current_substr)
                print(c + NUM_DISTINCT_CHARACTERS)
                break


if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
