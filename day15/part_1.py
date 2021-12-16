import sys
sys.path.append("..")

import utils_func.file
from utils_func.grid import Grid
from utils_func.graphs import dijkstra_length

def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    grid = Grid.parse(lines)
    dict =  grid.to_graph()
    print('Solution : {}'.format(dijkstra_length(dict, (0,0), (grid._width - 1, grid._height - 1))))
    # 745
    return 0

if __name__ == '__main__':
    sys.exit(main())
