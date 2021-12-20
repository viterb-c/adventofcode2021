from os import WUNTRACED
import sys
import sys
import heapq
import itertools
import re
import ast
from collections import defaultdict, Counter, deque

sys.path.append("..")
from utils_func.grid import Grid
import utils_func.file

def get_pixel(image: set, img_enhancement: str, y: int, x: int, wmin, wmax, hmin, hmax, ligths):
    pixel = ''
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if ligths == True and (y+j < wmin or y+j > wmax or x+i < hmin or x+i > hmax):
                pixel += '1'
            elif (y+j, x+i) not in image:
                pixel += '0'
            else:
                pixel += '1'
    return img_enhancement[int(pixel,2)]


def debug_dict(img, min_h, min_w, height, width):
    for y in range(min_h - 2, height + 2):
        for x in range(min_w - 2, width + 2):
            if (y,x) in img:
                print('#', end='')
            else:
                print('.', end='')
        print()

def get_image(lines: list) -> set:
    input = set()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                input.add((y,x))
    return input

def apply_enhancement(input: set, img_enhancement: str, all_light: bool):
    wmin = min([r for r,c in input])
    wmax = max([r for r,c in input])
    hmin = min([c for r,c in input])
    hmax = max([c for r,c in input])
    output = set()
    for y in range(wmin - 1, wmax + 2):
        for x in range(hmin - 1, hmax + 2):
            if get_pixel(image, img_enhancement, y, x, wmin, wmax, hmin , hmax, all_light) == '#':
                output.add((y,x))
    return output

lines = utils_func.file.get_lines(sys.argv[1])
img_enhancement = lines[0]
image = get_image(lines[2:])
for step in range(50):
    if step == 2:
        print('Part 1 : {}'.format(len(image)))
        # 5498
    image = apply_enhancement(image, img_enhancement, step % 2 != 0)
print('Part 2 : {}'.format(len(image)))
# 16014

