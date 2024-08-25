from collections import deque, defaultdict

class Edge:
    def __init__(self, src, des):
        self.src = src
        self.des = des

def create_graph():
    graph = defaultdict(list)
    
    graph[1].append(Edge(1, 2))
    graph[1].append(Edge(1, 3))
    graph[1].append(Edge(1, 4))

    graph[2].append(Edge(2, 1))
    graph[2].append(Edge(2, 5))
    graph[2].append(Edge(2, 6))

    graph[3].append(Edge(3, 1))
    graph[3].append(Edge(3, 4))
    graph[3].append(Edge(3, 5))
    graph[3].append(Edge(3, 6))

    graph[4].append(Edge(4, 1))
    graph[4].append(Edge(4, 3))
    graph[4].append(Edge(4, 6))

    graph[5].append(Edge(5, 2))
    graph[5].append(Edge(5, 3))

    graph[6].append(Edge(6, 2))
    graph[6].append(Edge(6, 3))
    graph[6].append(Edge(6, 4))
    
    return graph

def bfs(graph, visited, start):
    q = deque([start])
    
    while q:
        current = q.popleft()
        if not visited[current]:
            print(current, end=" ")
            visited[current] = True
            for edge in graph[current]:
                if not visited[edge.des]:
                    q.append(edge.des)

def main_bfs():
    v = 7  # Number of nodes (1 through 6)
    graph = create_graph()
    visited = [False] * v
    
    # BFS from each node
    for i in range(1, v):
        if not visited[i]:
            bfs(graph, visited, i)

if __name__ == "__main__":
    main_bfs()
