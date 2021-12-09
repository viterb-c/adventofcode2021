import sys
import math

sys.path.append("..")
import utils_func


def find_size_basin(positions: list, coord_basin: list, x: int, y: int) -> int:
    if x < 0 or y < 0 or y >= len(positions) or x >= len(positions[y]) or (x,y) in coord_basin or int(positions[y][x]) == 9:
        return 0
    coord_basin.append((x,y))
    return 1 + find_size_basin(positions, coord_basin, x + 1, y) + find_size_basin(positions, coord_basin, x - 1, y) + find_size_basin(positions, coord_basin, x, y + 1) + find_size_basin(positions, coord_basin, x, y - 1)

def sum_low_points(positions: list):
    sum = 0
    coord_basin = []
    size_basin = []
    for y in range(len(positions)):
        for x in range(len(positions[y])):
            if int(positions[y][x]) != 9 and (x,y) not in coord_basin:
                size_basin.append(find_size_basin(positions, coord_basin, x, y))
    size_basin.sort(reverse=True)
    return size_basin[0] * size_basin[1] * size_basin[2]

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(sum_low_points(lines)))
    # 1397760
    return 0

if __name__ == '__main__':
    sys.exit(main())
