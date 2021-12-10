import sys
import math

sys.path.append("..")
import utils_func

SCORES = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4
}

OPEN = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

def get_score(stack: list) -> int:
    score = 0
    i = len(stack) - 1
    for char in reversed(stack):
        score = score * 5 + SCORES[char]
    return score

def get_score_line(line: str, scores: list) -> int:
    stack = []
    for i in range(len(line)):
        if line[i] in OPEN:
            stack.append(line[i])
        elif OPEN[stack.pop()] != line[i]:
            return
    scores.append(get_score(stack))

def get_total_score(lines: list) -> int:
    scores = []
    for line in lines:
        get_score_line(line, scores)
    scores.sort()
    return scores[len(scores) // 2]

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    print('Solution : {}'.format(get_total_score(lines)))
    # 2292863731
    return 0

if __name__ == '__main__':
    sys.exit(main())
