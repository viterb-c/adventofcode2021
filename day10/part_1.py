import sys
import math

sys.path.append("..")
import utils_func

SCORES = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

OPEN = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

def check_syntax_error(line: str) -> int:
    stack = []
    for i in range(len(line)):
        if line[i] in OPEN:
            stack.append(line[i])
        elif OPEN[stack.pop()] != line[i]:
            return SCORES[line[i]]
    return 0

def get_total_syntax_error(lines: list) -> int:
    sum = 0
    for line in lines:
        sum += check_syntax_error(line)
    return sum

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(get_total_syntax_error(lines)))
    # 415953
    return 0

if __name__ == '__main__':
    sys.exit(main())
