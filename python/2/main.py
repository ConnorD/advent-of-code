import sys

RPS_WINS = {
    'A': 'B',
    'B': 'C',
    'C' : 'A',
}
RPS_LOSSES = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}
RPS_EXTRA_SCORE = {
    'A': 1,
    'B': 2,
    'C': 3,
}

def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    my_score = 0
    for l in lines:
        if l[2] == 'X':
            my_choice = RPS_LOSSES[l[0]]
        elif l[2] == 'Y':
            my_choice = l[0]
            my_score += 3
        elif l[2] == 'Z':
            my_choice = RPS_WINS[l[0]]
            my_score += 6

        my_score += RPS_EXTRA_SCORE[my_choice]
    
    print(my_score)

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
