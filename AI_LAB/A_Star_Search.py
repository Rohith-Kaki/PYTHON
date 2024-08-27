from collections import defaultdict
from heapq import heapify, heappop, heappush
from platform import node

class Edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight

def create_graph():
    graph = defaultdict(list)
    
    graph[0].append(Edge(0, 1, 1))
    graph[0].append(Edge(0, 5, 10))

    graph[1].append(Edge(1, 2, 2))
    graph[1].append(Edge(1, 3, 1))

    graph[2].append(Edge(2, 4, 5))

    graph[3].append(Edge(3, 4, 3))
    graph[3].append(Edge(3, 5, 4))

    graph[4].append(Edge(4, 5, 2))

    return graph

def A_star(graph, start, goal, hcost):
    nodes = []
    heapify(nodes)
    # this heap will pop the tuple with lowest fcost first..
    heappush(nodes, (0 + hcost[start][1], start, [start]))
    visited = set()
    while nodes:
        f_cost , currentnode, path = heappop(nodes)
        if currentnode in visited:
            continue
        visited.add(currentnode)
        if(currentnode == goal):
            return path, f_cost
        for edge in graph[currentnode]:
            if edge.des not in visited:
                g_cost = f_cost - hcost[start][1] + edge.weight
                heappush(nodes, (g_cost+hcost[edge.des][1], edge.des, path + [edge.des]))
    return None, float("inf") # Return None and inf cost if the goal is not reachable
def main():
    v = 6
    graph = create_graph()
    start = 0
    goal = 5
    hcost = [[0,5],
             [1,3],
             [2,4],
             [3,2],
             [4,6],
             [5,0]]
    path, f_cost = A_star(graph, start, goal, hcost)
    if path:
        print("Path found:", " -> ".join(map(str, path)))
        print(f"PathCost: {f_cost}")
        
    else:
        print("No path found")


if __name__ == "__main__":
    main()
