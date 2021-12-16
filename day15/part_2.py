import sys
sys.path.append("..")

import utils_func.file
from utils_func.grid import Grid
from utils_func.graphs import dijkstra_length

def transform_grid(grid):
    len_x = len(grid[0])
    len_y = len(grid)
    for y_resize in range(0, 5):
        for x_resize in range(0, 5):
            resize = y_resize + x_resize
            if resize == 0:
                continue
            min_x = x_resize * len_x
            min_y = y_resize * len_y 
            max_x = (1 + x_resize) * len_x
            max_y = (1 + y_resize) * len_y
            for y in range(min_y, max_y):
                if y >= len(grid):
                    grid.append([])
                for x in range(min_x, max_x):
                    value = grid[y % 100][x % 100]
                    grid[y].append(value + resize if value + resize <= 9 else (value + resize) % 9)
    return Grid(grid)

def main() -> int:
    lines = utils_func.file.get_lines(sys.argv[1])
    grid = Grid.parse(lines)
    grid = transform_grid(grid._grid)
    dict =  grid.to_graph()
    print('Solution : {}'.format(dijkstra_length(dict, (0,0), (grid._width - 1, grid._height - 1))))
    # 3002
    return 0

if __name__ == '__main__':
    sys.exit(main())
