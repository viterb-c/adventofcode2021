import sys
import math

sys.path.append("..")
import utils_func

def is_digit_1_4_7_8(digit: str) -> bool:
    if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
        return True
    return False

def get_digits(lines: list):
    digits = 0
    for line in lines:
        output = line.split('|')[1].split()
        digits += len([x for x in filter(is_digit_1_4_7_8, output)])
    return digits

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(get_digits(lines)))
    # 421
    return 0

if __name__ == '__main__':
    sys.exit(main())
