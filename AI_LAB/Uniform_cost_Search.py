from heapq import heappop, heappush
from collections import defaultdict

class Edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight

def create_graph():
    graph = defaultdict(list)
    
    # Example graph
    graph[0].append(Edge(0, 1, 5))
    graph[0].append(Edge(0, 3, 10))
    
    graph[1].append(Edge(1, 4, 15))
    graph[1].append(Edge(1, 2, 4))
    
    graph[2].append(Edge(2, 5, 8))
    
    graph[3].append(Edge(3, 4, 11))
    
    graph[4].append(Edge(4, 5, 4))
    
    return graph

def uniform_cost_search(graph, start, goal):
    # Priority queue for UCS, stores (cost, current_node, path)
    priority_queue = []
    heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:
        cost, current_node, path = heappop(priority_queue)
        if current_node == goal:
            return cost, path
        if current_node not in visited:
            visited.add(current_node)
            for edge in graph[current_node]:
                if edge.des not in visited:
                    new_cost = cost + edge.weight
                    heappush(priority_queue, (new_cost, edge.des, path + [edge.des]))

    return float("inf"), []  # Return inf cost and empty path if goal is not reachable

def main():
    graph = create_graph()
    start = 0
    goal = 5
    
    cost, path = uniform_cost_search(graph, start, goal)
    
    if cost < float("inf"):
        print(f"Shortest path from node {start} to node {goal} has cost {cost}: {path}")
    else:
        print(f"Goal node {goal} is not reachable from start node {start}")

if __name__ == "__main__":
    main()
