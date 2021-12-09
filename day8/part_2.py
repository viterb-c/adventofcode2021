import sys
import math

sys.path.append("..")
import utils_func

def find_by_length(inputs: list, length: int, digits: list) -> str:
    for digit in inputs:
        if len(digit) == length and digit not in digits:
            return digit

def find_by_pattern(inputs: list, target: str, digits: list, length: int) -> str:
    for digit in inputs:
        if (len(set(digit) - set(target))) == length and digit not in digits:
            return digit

def find_digits(inputs: list) -> list:
    digits = [''] * 10
    digits[1] = find_by_length(inputs, 2, digits)
    digits[4] = find_by_length(inputs, 4, digits)
    digits[7] = find_by_length(inputs, 3, digits)
    digits[8] = find_by_length(inputs, 7, digits)
    digits[6] = find_by_pattern(filter(lambda x: len(x) == 6, inputs), digits[1], digits, 5) 
    digits[3] = find_by_pattern(filter(lambda x: len(x) == 5, inputs), digits[1], digits, 3) 
    digits[9] = find_by_pattern(filter(lambda x: len(x) == 6, inputs), digits[3], digits, 1) 
    digits[0] = find_by_length(inputs, 6, digits)
    digits[2] = find_by_pattern(filter(lambda x: len(x) == 5, inputs), digits[6], digits, 1)
    digits[5] = find_by_length(inputs, 5, digits)
    return digits

def get_int_output(output: list, digits: list) -> int:
    str_output = ''
    for digit in output:
        ordered_digit = ''.join(sorted(digit))
        str_output += str(digits.index(ordered_digit))
    return int(str_output)

def get_digits(lines: list):
    sum = 0
    for line in lines:
        inputs = line.split('|')[0].split()
        outputs = line.split('|')[1].split()
        digits = find_digits(inputs)
        ordered_digit = [''.join(sorted(x)) for x in digits]
        sum += get_int_output(outputs, ordered_digit)
    return sum

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(get_digits(lines)))
    # 986163
    return 0

if __name__ == '__main__':
    sys.exit(main())
