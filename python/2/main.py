RPS_WINS = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
}

RPS_TIES = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

RPS_EXTRA_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    my_score = 0
    for l in lines:
        my_score += RPS_EXTRA_SCORE[l[2]]

        if RPS_WINS[l[2]] == l[0]:
            my_score += 6
        elif RPS_TIES[l[2]] == l[0]:
            my_score += 3
    
    print(my_score)

if __name__ == '__main__':
    main()
