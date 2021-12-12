import sys

sys.path.append("..")
import utils_func

def get_all_path(current_point: str, graph: dict, paths: list, current_path):
    current_path.append(current_point)
    if current_point == 'end':
        paths.append(current_path)
        return
    for point in graph[current_point]:
        if point in current_path and point.islower() == True:
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
    # 5252
    return 0

if __name__ == '__main__':
    sys.exit(main())
