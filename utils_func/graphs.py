
from collections import defaultdict


def add_points(graph: dict, start: str, end: str):
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]


def get_graph(lines: list, delimiter: str) -> dict:
    graph = {}
    for line in lines:
        points = line.split(delimiter)
        add_points(graph, points[0], points[1])
        add_points(graph, points[1], points[0])
    return graph
         
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)

    def build_graph(self, lines: list, delimiter: str) -> dict:
        for line in lines:
            points = line.split(delimiter)
            self.add_edge(points[0], points[1])
            self.add_edge(points[1], points[0])
    


def dijkstra_length(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while len(queue) > 0:
        current_node, current_distance = queue.pop(0)
        if current_node == end:
            return current_distance
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor_node, neighbor_distance in graph[current_node]:
            queue.append((neighbor_node, current_distance + neighbor_distance))
        queue = sorted(queue, key=lambda node: node[1])