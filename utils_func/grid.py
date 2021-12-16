import itertools

class Grid:
    def __init__(self, grid):
        self._grid = grid
        self._width = len(self._grid[0])
        self._height = len(self._grid)

    @staticmethod
    def parse(s):
        grid = []
        for line in s:
            grid.append(list(map(int, line)))
        return Grid(grid)

    def neighbors(self, x, y, diagonals=False):
        assert(0 <= x < self._width and 0 <= y < self._height)
        if diagonals:
            for nx, ny in itertools.product((x-1, x, x+1), (y-1, y, y+1)):
                if x == nx and y == ny:
                    continue
                if 0 <= nx < self._width and 0 <= ny < self._height:
                    yield nx, ny
        else:
            if 0 < x:
                yield x - 1, y
            if x + 1 < self._width:
                yield x + 1, y
            if 0 < y:
                yield x, y - 1
            if y + 1 < self._height:
                yield x, y + 1

    def to_dict(self):
        return {(x,y): value 
                for x,col in enumerate(self._grid) 
                for y, value in enumerate(col)}

    def to_graph(self):
        graph = {}
        for x, col in enumerate(self._grid):
            for y, val in enumerate(col):
                links = []
                for i,j in self.neighbors(x,y):
                    value = self._grid[i][j]
                    links.append(((i,j), value))  
                graph[(x,y)] = links
        return graph