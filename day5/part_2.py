import sys
import math

sys.path.append("..")
import utils_func
from utils_func.coordinates import Coordinates

def parse_coordinates(line: str) -> tuple:
    coord = line.split(' -> ')
    begin = coord[0].split(',')
    end = coord[1].split(',')
    return (Coordinates(int(begin[0]), int(begin[1])),
            Coordinates(int(end[0]), int(end[1])))

def check_coordinates(coord_dict, x, y):
    coord = Coordinates(x, y)
    if coord in coord_dict:
        coord_dict[coord] += 1
    else:
        coord_dict[coord] = 1

def vertical_line(coord_dict: dict, x: int, y_start: int, y_end: int):
    y = y_start
    increment = -1 if y_start > y_end else 1
    while y != y_end:
        check_coordinates(coord_dict, x, y)
        y += increment
    check_coordinates(coord_dict, x, y)

def horizontal_line(coord_dict: dict, y: int, x_start: int, x_end: int):
    x = x_start
    increment = -1 if x_start > x_end else 1
    while x != x_end:
        check_coordinates(coord_dict, x, y)
        x += increment
    check_coordinates(coord_dict, x, y)

def diagonale_line(coord_dict: dict, begin, end):
    x = begin.x
    y = begin.y 
    increment_x = -1 if begin.x > end.x else 1
    increment_y = -1 if begin.y > end.y else 1
    while x != end.x and y != end.y:
        check_coordinates(coord_dict, x, y)
        x += increment_x
        y += increment_y
    check_coordinates(coord_dict, x, y)

def get_overlap(lines: list) -> dict:
    coord_dict = {}
    for line in lines:
        tuple_coordinates = parse_coordinates(line)
        begin = tuple_coordinates[0]
        end = tuple_coordinates[1]
        if begin.x == end.x:
            vertical_line(coord_dict, begin.x, begin.y, end.y)
        elif begin.y == end.y:
            horizontal_line(coord_dict, begin.y, begin.x, end.x)
        elif abs(begin.x - end.x) == abs(begin.y - end.y):
            diagonale_line(coord_dict, begin, end)
    return coord_dict

def get_number_overlaps(overlaps: dict) -> int:
    nbr = 0
    for key, value in overlaps.items():
        if value > 1:
            nbr += 1
    return nbr

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    overlaps = get_overlap(lines)
    print('Solution : {}'.format(get_number_overlaps(overlaps)))
    # 21305
    return 0

if __name__ == '__main__':
    sys.exit(main())