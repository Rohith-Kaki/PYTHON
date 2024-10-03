import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstset):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and mstset[v] == False:
                min_val = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V  # Initialize all keys as infinite
        parent = [None] * self.V  # Array to store the constructed MST
        key[0] = 0  # Make key 0 so that this vertex is picked as the first vertex
        mstset = [False] * self.V  # To represent the set of vertices not yet included in MST
        parent[0] = -1  # First node is always the root of the MST

        for count in range(self.V):
            u = self.minKey(key, mstset)  # Pick the minimum key vertex from the set of vertices not yet included in MST
            mstset[u] = True  # Add the picked vertex to the MST set

            for v in range(self.V):
                # Update key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstset[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()
