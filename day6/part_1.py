import sys
import math

sys.path.append("..")
import utils_func

def number_lanternfish(fishes) -> int:
    for day in range(80):
        new_fishes = []
        for i in range(len(fishes)):
            if fishes[i] == 0:
                new_fishes.append(8)
                fishes[i] = 6
            else:
                fishes[i] -= 1
        fishes = fishes + new_fishes
    return len(fishes)

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(number_lanternfish([int(i) for i in lines[0].split(',')])))
    # 352195
    return 0

if __name__ == '__main__':
    sys.exit(main())