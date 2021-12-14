from collections import Counter
import sys

sys.path.append("..")
import utils_func

def get_rules(lines: list) -> dict:
    dict_rules = {}
    for line in lines:
        dict_rules[line[0] + line[1]] = line[-1]
    return dict_rules

def run_steps(template: str, rules: dict) -> str:
    letters = Counter(template)
    pairs = Counter([a + b for a,b in zip(template, template[1:])])
    for _ in range(40):
        old_pairs = pairs.copy()
        for (a,b),c in rules.items():
            count = old_pairs[a+b]
            pairs[a+b] -= count
            pairs[a+c] += count
            pairs[c+b] += count
            letters[c] += count
    return letters

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    rules = get_rules(lines[2:])
    letters = run_steps(lines[0], rules)
    print('Solution : {}'.format(letters.most_common()[0][1] - letters.most_common()[-1][1]))
    # 2112
    return 0

if __name__ == '__main__':
    sys.exit(main())
