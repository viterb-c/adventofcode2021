import sys

sys.path.append("..")
import utils_func

def get_sum(lines, index) -> int:
    sum = 0
    for i in range(index, index + 3):
        sum += int(lines[i])
    return sum

def get_increased_sums(lines) -> int: 
    sum_depth_increase = 0
    prev_sum = get_sum(lines, 0)
    for index in range(1, len(lines) - 2):
        sum = get_sum(lines, index)
        if prev_sum < sum:
            sum_depth_increase += 1
        prev_sum = sum
    return sum_depth_increase

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print("Solution : {}".format(get_increased_sums(lines)))
    # 1429
    return 0

if __name__ == '__main__':
    sys.exit(main())