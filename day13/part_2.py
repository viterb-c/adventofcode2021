import sys
from operator import itemgetter

sys.path.append("..")
import utils_func


def fold_x(x: int, dot: tuple):
    dot_x = dot[0]
    if dot_x < x:
        return dot
    return (2 * x - dot[0], dot[1])


def fold_y(y: int, dot: tuple):
    dot_y = dot[1]
    if dot_y < y:
        return dot
    return (dot[0], 2 * y - dot[1])

def apply_fold(dots: list, folds: str):
    dots_visible = set()
    for dot in dots:
        if folds.find('y') != -1:
            y = int(folds[folds.index('y') + 2:])
            dots_visible.add(fold_y(y, dot))
        else:
            x = int(folds[folds.index('x') + 2:])
            dots_visible.add(fold_x(x, dot))
    return dots_visible

def get__visible_dots(dots: list, folds: list) -> list:
    dots = [(int(dot.split(',')[0]), int(dot.split(',')[1])) for dot in dots]
    for fold in folds:
        dots = list(apply_fold(dots, fold))
    return dots

def display_dots(dots: list):
    max_x = max(dots, key=itemgetter(0))[0]
    max_y = max(dots, key=itemgetter(1))[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in dots:
                print('O', end='')
            else:
                print(' ', end='')
        print('')

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    dots = lines[:lines.index('')]
    folds = lines[lines.index('') + 1:]
    visible_dots = get__visible_dots(dots, folds)
    display_dots(visible_dots)
    # LKREBPRK
    return 0

if __name__ == '__main__':
    sys.exit(main())
