from collections import defaultdict

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

def dfs(graph, curr, visited):
    print(curr, end=" ")
    visited[curr] = True
    
    for edge in graph[curr]:
        if not visited[edge.des]:
            dfs(graph, edge.des, visited)

def main_dfs():
    v = 7  # Number of nodes (1 through 6)
    graph = create_graph()
    visited = [False] * v
    
    # DFS from each node
    for i in range(1, v):
        if not visited[i]:
            dfs(graph, i, visited)

if __name__ == "__main__":
    main_dfs()
