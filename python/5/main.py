import sys


def main(argv):
    with open(f'{argv[0]}.txt') as f:
        lines = f.readlines()

    

if __name__ == '__main__':
    main(sys.argv[1:] if len(sys.argv) > 1 else ['input'])
