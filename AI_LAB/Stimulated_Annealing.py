# SIMULATED ANNEALING
import random
import math

# Define the objective function
def objective_function(state):
    x, y = state
    return x*2 + y*2

# Define the simulated annealing algorithm
def simulated_annealing(initial_state, max_iterations, cooling_rate, initial_temperature):
    current_state = initial_state
    current_objective = objective_function(current_state)
    best_state = current_state
    best_objective = current_objective
    temperature = initial_temperature

    for iteration in range(max_iterations):
        # Generate a new state by perturbing the current state
        new_state = (current_state[0] + random.uniform(-0.1, 0.1), current_state[1] + random.uniform(-0.1, 0.1))

        # Calculate the change in objective function
        delta_objective = objective_function(new_state) - best_objective

        # Accept the new state if it's better, or with a probability based on the temperature
        if delta_objective < 0 or random.random() < math.exp(-delta_objective / temperature):
            current_state = new_state
            current_objective = objective_function(current_state)
            if current_objective < best_objective:
                best_state = current_state
                best_objective = current_objective

        # Update the temperature
        temperature *= (1 - iteration / max_iterations)

        # Print the current state and objective function value
        print(f"Iteration {iteration+1}: State = {current_state}, Objective = {current_objective:.4f}")

    return best_state, best_objective

# Run the simulated annealing algorithm
initial_state = (10, 10)
max_iterations = 100
cooling_rate = 0.01
initial_temperature = 100

best_state, best_objective = simulated_annealing(initial_state, max_iterations, cooling_rate, initial_temperature)

print(f"Final State: {best_state}, Final Objective: {best_objective:.4f}")