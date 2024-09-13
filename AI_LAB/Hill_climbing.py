def hill_climbing(G, S, f, g):
    # G: Graph represented as an adjacency list {node: [(adjacent_node, cost), ...]}
    # S: Initial state (starting node)
    # f: Objective function value for the initial state
    # g: Goal state
    if S == g:
        return "Success", f
    
    fmax = f
    current_state = S
    
    for (u, cost) in G[S]:
        f_adj = cost  # Assuming f_adj(u) is the cost to reach the adjacent node u
        
        if f_adj > fmax:
            fmax = f_adj
            current_state = u
            
    if current_state != S:
        return hill_climbing(G, current_state, fmax, g)
    
    return "No better state found", fmax

# Example Usage
G = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 6)],
    'D': [],
    'E': [],
    'F': []
}
S = 'A'
f = 0  # Initial objective function value (can be adjusted)
g = 'F'

result, fmax = hill_climbing(G, S, f, g)
print("Result:", result)
print("Maximum Objective Function Value:", fmax)