import sys


def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    overlapping_pairs = 0

    def _assignment_range(assignment_literal: str) -> set:
        return range(int(assignment_literal.split('-')[0]), int(assignment_literal.split('-')[1]))

    for l in lines:
        assignment_literal_1, assignment_literal_2 = l.split(',')
        print(assignment_literal_1, assignment_literal_2)
        assignment_range_1 = _assignment_range(assignment_literal_1)
        assignment_range_2 = _assignment_range(assignment_literal_2)

        if len(set(assignment_range_1).intersection(assignment_range_2)) > 0:
            overlapping_pairs += 1

    print(overlapping_pairs)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
