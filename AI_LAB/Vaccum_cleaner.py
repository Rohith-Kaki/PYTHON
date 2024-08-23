import numpy as np
transition_table = [[0,1,0],
                    [0,1,1],
                    [2,3,0],
                    [2,3,3],
                    [4,5,4],
                    [4,5,1],
                    [6,7,4],
                    [6,7,3]]

seq_action = [[0,1,1,1,1,2,2,2,2,1],
              [0,2,1,2,2,2,1,1,1,0],
              [0,0,0,0,0,1,1,1,1,2],
              [2,2,2,2,2,2,1,1,1,0],
              [0,1,1,1,1,2,2,2,2,1],
              [0,2,1,2,2,2,1,1,1,0],
              [0,0,0,0,0,1,1,1,1,2],
              [2,2,2,2,2,2,1,1,1,0],
              [0,0,0,0,0,1,1,1,1,2],
              [2,2,2,2,2,2,1,1,1,0]]
seq_action1 = []
duration = 10

# using random generator
for i in range(0,11):
    seq = np.random.randint(0,3,duration)
    seq_action1.append(seq)

goal_state = [0,1]

current_state = int(input("Enter inital state:"))
for seq in seq_action:
    t = 0
    path_cost = 0
    while(t<duration):
        action = seq[t]
        next_state = transition_table[current_state][action]
        path_cost += 1
        current_state = next_state
        print(current_state)
        t += 1
    print(f"sequence cost = {path_cost}")
    if (current_state == goal_state[0] or current_state == goal_state[1]):
        print("reached goal")
    else:
        print("Goal not reached")

