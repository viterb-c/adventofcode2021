import sys

sys.path.append("..")
import utils_func
from collections import Counter

def cant_pass(current_pass: list, point: str):
    double_lower = [key for key in Counter(current_pass).keys() if Counter(current_pass)[key] > 1 and key.islower()]    
    if point == 'start' or (len(double_lower) > 0 and point in current_pass):
        return True
    return False

def get_all_path(current_point: str, graph: dict, paths: list, current_path):
    current_path.append(current_point)
    if current_point == 'end':
        paths.append(current_path)
        return
    for point in graph[current_point]:
        if point.islower() and cant_pass(current_path, point):
            pass
        else:
            get_all_path(point, graph, paths, current_path.copy())

def get_number_paths(graph: dict) -> int:
    paths = []
    get_all_path('start', graph, paths, [])
    return len(paths)

def main() -> int:
    lines = utils_func.get_lines(sys.argv[1])
    graph = utils_func.get_graph(lines, '-')
    print('Solution : {}'.format(get_number_paths(graph)))
    # 147784
    return 0

if __name__ == '__main__':
    sys.exit(main())
