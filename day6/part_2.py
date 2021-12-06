import sys
import math

sys.path.append("..")
import utils_func

def initial_fishes(init_fish, lanternfishes):
    for fish in init_fish:
        lanternfishes[fish] += 1


def populate(lanternfishes: list, period: int):
    for day in range(period):
        reproduction = lanternfishes.pop(0)
        lanternfishes.append(reproduction)
        lanternfishes[6] += reproduction

def number_lanternfish(fishes) -> int:
    lanternfishes = [0] * 9
    initial_fishes(fishes, lanternfishes)
    populate(lanternfishes, 256)
    return sum(lanternfishes)

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(number_lanternfish([int(i) for i in lines[0].split(',')])))
    # 1600306001288
    return 0

if __name__ == '__main__':
    sys.exit(main())
