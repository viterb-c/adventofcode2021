import sys
import re
sys.path.append("..")

import utils_func.file

def get_area(line: str):
    TRENCH_REGEX = r'target area: x=(\d+)\.\.(\d+), y=(-\d+)\.\.(-\d+)'
    match = re.match(TRENCH_REGEX, line)
    coords = tuple(int(match.group(i)) for i in range(1, 5))
    return coords

def trajectory_y(vy: int, min_area: int, max_area: int) -> int:
    y = 0
    max_y = 0
    while True:
        y += vy
        max_y = max(max_y, y)
        vy -= 1
        if min_area <= y and y <= max_area:
            return max_y
        elif y < min_area:
            return 0

def get_max_y(min_area_y: int, max_area_y: int):
    max_y = 0
    for vy in range(200):
        max_y = max(trajectory_y(vy, min_area_y, max_area_y), max_y)
    return max_y
                


def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    coords = get_area(lines[0])
    print("Solution : {}".format(get_max_y(coords[2], coords[3])))
    # 6555
    return 0

if __name__ == '__main__':
    sys.exit(main())
