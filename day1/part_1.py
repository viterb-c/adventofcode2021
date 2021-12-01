import sys

sys.path.append("..")
import utils_func

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    depth_increase = 1 
    for index in range(1, len(lines)):
        if lines[index] > lines[index - 1]:
            depth_increase += 1
    print("Solution : {}".format(depth_increase))
    # 1400
    return 0

if __name__ == '__main__':
    sys.exit(main())