from typing import List, Tuple, Any

class Vertex:
    def __init__(self, row: int, column: int, v: int):
        self.row = row
        self.column = column
        self.v = v

    def __repr__(self) -> str:
        return f"({self.row},{self.column})"

class Graph:
    def __init__(self):
        self.data = {}

    def adjacent(self, x: Vertex, y: Vertex) -> bool:
        return y in self.data[x] or x in self.data[y]

    def neighbors(self, x: Vertex):
        return self.data[x]

    def add_vertex(self, x: Vertex):
        if not self.data.get(x, None):
            self.data[x] = set()

    def remove_vertex(self, x: Vertex):
        self.data.pop(x, None)

    def add_edge(self, x: Vertex, y: Vertex):
        self.add_vertex(x)
        self.add_vertex(y)
        if y not in self.data[x]:
            self.data[x].add(y)

    def remove_edge(self, x: Vertex, y: Vertex):
        self.data[x].add(y)
        self.data[y].add(x)

    def get_vertex_value(self, x: Vertex) -> int:
        return x.v

    def set_vertex_value(self, x: Vertex, v: int):
        x.v = v
    
def read_input(path: str) -> str:
    with open(path, "r") as f:
        output = f.read()
    return output

def str_to_int(x: str) -> int:
    if x == "S":
        x = "a"
    elif x == "E":
        x = "z"
    return list("abcdefghijklmnopqrstuvwxyz").index(x)

def valid_index(row: int, column: int, data: List[List[int]]) -> bool:
    if row < 0 or column < 0:
        return False
    try:
        data[row][column]
        return True
    except:
        return False

def parse_input(txt_block: str) -> Graph:
    data = []
    for i, row in enumerate(txt_block.split("\n")):
        if row:
            temp = []
            for j, value in enumerate(list(row)):
                temp.append(Vertex(i, j, str_to_int(value)))
            data.append(temp)
    graph = Graph()
    for i in range(len(data)):
        for j in range(len(data[0])):
            current_vertex = data[i][j]
            if valid_index(i+1, j, data):
                temp_vertex = data[i+1][j] # Down
                if temp_vertex.v - current_vertex.v <= 1:
                    graph.add_edge(current_vertex, temp_vertex)
            if valid_index(i-1, j, data):
                temp_vertex = data[i-1][j] # Up
                if temp_vertex.v  - current_vertex.v <= 1:
                    graph.add_edge(current_vertex, temp_vertex)
            if valid_index(i, j+1, data):
                temp_vertex = data[i][j+1] # Right
                if temp_vertex.v - current_vertex.v <= 1:
                    graph.add_edge(current_vertex, temp_vertex)
            if valid_index(i, j-1, data):
                temp_vertex = data[i][j-1] # Left
                if temp_vertex.v - current_vertex.v <= 1:
                    graph.add_edge(current_vertex, temp_vertex)
    return graph

def dijkstra(graph: Graph, start: Tuple[int, int], end: Tuple[int, int]):
    start_node = next(iter([i for i in graph.data.keys() if i.row == start[0] and i.column == start[1]]))
    end_node = next(iter([i for i in graph.data.keys() if i.row == end[0] and i.column == end[1]]))
    Q = []
    dist = {}
    prev = {}
    
    for v in graph.data.keys():
        dist[v] = float('inf')
        prev[v] = None
        Q.append(v)
    dist[start_node] = 0

    while Q:
        min_dist = min([dist[v] for v in Q])
        u = next(iter([i for i in Q if dist[i] == min_dist]))
        Q.remove(u)

        for v in [i for i in graph.neighbors(u) if i in Q]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

        if u == end_node:
            break

    output = []
    u = end_node
    if prev.get(u) or u == start:
        while u:
            output.append(u)
            u = prev.get(u, None)
    return output[::-1]
            
def get_path(graph: Graph, c1: Tuple[int, int], c2: Tuple[int, int]) -> List[Any]:
    #  start_row, start_col = c1
    #  end_row, end_col = c2
    #  start_node = next(iter([i for i in graph.data.keys() if i.row == start_row and i.column == start_col]))
    #  end_node = next(iter([i for i in graph.data.keys() if i.row == end_row and i.column == end_col]))
    #  g = DGraph()
    for key, neighbors in graph.data.items():
        for n in neighbors:
            g.add_edge(key, n, 1)
    dijkstra = DijkstraSPF(g, start_node)
    return dijkstra.get_path(end_node)

def p1():
    txt_block = read_input("input.txt")
    graph = parse_input(txt_block)
    path = dijkstra(graph, (20,0), (20,55))
    print(f"P1: {len(path)-1}")

def p2():
    txt_block = read_input("input.txt")
    graph = parse_input(txt_block)
    starting_points = [i for i in graph.data.keys() if i.v == 0]
    path_lens = []
    for p in starting_points:
        try: 
            path_lens.append(len(dijkstra(graph, (p.row,p.column), (20,55))))
        except:
            continue
    print(f"P2: {min(path_lens)-1}")

def test():
    txt_block = read_input("test.txt")
    graph = parse_input(txt_block)
    path = dijkstra(graph, (0, 0), (2, 5))
    print(f"Test: {len(path)-1}")

if __name__ == "__main__":
    p1()
    p2()
    test()
