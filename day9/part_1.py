import sys
import math

sys.path.append("..")
import utils_func


def is_adj_locations_inferior(positions: list, x: int, y: int, height: int) -> bool:
    if x < 0 or y < 0 or y >= len(positions) or x >= len(positions[y]):
        return True
    return positions[y][x] > height

def is_low_point(positions: list, x: int, y: int) -> bool:
    height = positions[y][x]
    return is_adj_locations_inferior(positions, x - 1, y, height) and is_adj_locations_inferior(positions, x + 1, y, height) and is_adj_locations_inferior(positions, x, y - 1, height) and is_adj_locations_inferior(positions, x, y + 1, height)

def sum_low_points(positions: list):
    sum = 0
    for y in range(len(positions)):
        for x in range(len(positions[y])):
            if is_low_point(positions, x, y):
                sum += (1 + int(positions[y][x]))
    return sum

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(sum_low_points(lines)))
    # 462
    return 0

if __name__ == '__main__':
    sys.exit(main())
