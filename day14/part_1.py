import sys

sys.path.append("..")
import utils_func

def get_dict(lines: list) -> dict:
    dict_pair = {}
    for line in lines:
        pair = line.split(' -> ')
        dict_pair[pair[0]] = pair[1]
    return dict_pair

def build_template(template: str, pairs: dict) -> str:
    new_template = ''
    for i in range(len(template)):
        new_template += template[i]
        if i + 2 <= len(template):
            new_template += pairs[template[i : i + 2]]
    return new_template

def run_steps(template: str, pairs: dict) -> str:
    for step in range(10):
        template = build_template(template, pairs)
    return template

def get_solution(template: str) -> int:
    sums = [template.count(char) for char in set(template)]
    sums.sort()
    return sums[-1] - sums[0]

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    pairs = get_dict(lines[2:])
    template = run_steps(lines[0], pairs)
    print('Solution : {}'.format(get_solution(template)))
    # 2112
    return 0

if __name__ == '__main__':
    sys.exit(main())
