import sys
import re
sys.path.append("..")

import utils_func.file

def get_area(line: str):
    TRENCH_REGEX = r'target area: x=(\d+)\.\.(\d+), y=(-\d+)\.\.(-\d+)'
    match = re.match(TRENCH_REGEX, line)
    coords = tuple(int(match.group(i)) for i in range(1, 5))
    return coords

def is_velocity_correct(vx: int, vy: int, area: tuple):
    x = 0
    y = 0
    while True:
        x += vx
        y += vy
        vy -= 1
        vx = vx - 1 if vx > 0 else 0
        if area[0] <= x and x <= area[1] and area[2] <= y and y <= area[3]:
            return True
        elif area[1] < x or y < area[2]:
            return False

def get_number_velocities(area: tuple) -> int:
    velocities = set()
    for vy in range(-500,500):
        for vx in range(0, 500):
            if is_velocity_correct(vx, vy, area) == True:
                velocities.add((vx,vy))
    return len(velocities)

def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    coords = get_area(lines[0])
    print("Solution : {}".format(get_number_velocities(coords)))
    # 4973
    return 0

if __name__ == '__main__':
    sys.exit(main())
