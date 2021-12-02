import sys

sys.path.append("..")
import utils_func

def navigate_submarine(intructions) -> int:
    depth = 0
    horizontal_position = 0
    for i in range(len(intructions)):
        if intructions[i][0] == 'f':
            horizontal_position += int(intructions[i][8:])
        elif intructions[i][0] == 'd':
            depth += int(intructions[i][5:])
        elif intructions[i][0] == 'u':
            depth -= int(intructions[i][3:])
    return depth * horizontal_position

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print("Solution : {}".format(navigate_submarine(lines)))
    # 1484118
    return 0

if __name__ == '__main__':
    sys.exit(main())