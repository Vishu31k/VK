def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    """
    Solves the water jug problem using Depth-First Search (DFS).

    Args:
        jug1_capacity: Capacity of the first jug.
        jug2_capacity: Capacity of the second jug.
        target: The desired amount of water in one of the jugs.

    Returns:
        A list of steps (jug1, jug2) to reach the target, or None if no solution is found.
    """

    def dfs(current_state, visited, path):
        """
        Recursive helper function for DFS.

        Args:
            current_state: The current state of the jugs (jug1, jug2).
            visited: A set to keep track of visited states.
            path: A list to store the path to the current state.
        """

        jug1, jug2 = current_state

        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            return path + [current_state]

        # Check if we have already visited this state
        if current_state in visited:
            return None

        visited.add(current_state)

        # Explore possible actions (fill, empty, pour)
        possible_actions = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (min(jug1_capacity, jug1 + jug2), max(0, jug1 + jug2 - jug1_capacity)),  # Pour from jug2 to jug1
            (max(0, jug1 + jug2 - jug2_capacity), min(jug2_capacity, jug1 + jug2)),  # Pour from jug1 to jug2
        ]

        # Recursively explore each possible action
        for action in possible_actions:
            result = dfs(action, visited.copy(), path + [current_state])
            if result:
                return result

        return None  # No solution found from this state

    # Start DFS from the initial state (0, 0)
    initial_state = (0, 0)
    solution = dfs(initial_state, set(), [])
    return solution

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2
solution = water_jug_dfs(jug1_capacity, jug2_capacity, target)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
