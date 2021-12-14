import sys

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

def apply_fold(dots_visible: set, dot: tuple, folds: str):
    if folds.find('y') != -1:
        y = int(folds[folds.index('y') + 2:])
        dots_visible.add(fold_y(y, dot))
    else:
        x = int(folds[folds.index('x') + 2:])
        dots_visible.add(fold_x(x, dot))

def get_number_visible_dots(dots: list, folds: list) -> int:
    dots = [(int(dot.split(',')[0]), int(dot.split(',')[1])) for dot in dots]
    dots_visible = set()
    for dot in dots:
        apply_fold(dots_visible, dot, folds[0])
    return len(dots_visible)

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    dots = lines[:lines.index('')]
    folds = lines[lines.index('') + 1:]
    print('Solution : {}'.format(get_number_visible_dots(dots, folds)))
    # 653
    return 0

if __name__ == '__main__':
    sys.exit(main())
