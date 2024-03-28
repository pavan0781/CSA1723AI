class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def successors(state):
    children = []
    if state.boat == 'left':
        children.extend([
            State(state.missionaries - 2, state.cannibals, 'right'),
            State(state.missionaries, state.cannibals - 2, 'right'),
            State(state.missionaries - 1, state.cannibals - 1, 'right'),
            State(state.missionaries - 1, state.cannibals, 'right'),
            State(state.missionaries, state.cannibals - 1, 'right')
        ])
    else:
        children.extend([
            State(state.missionaries + 2, state.cannibals, 'left'),
            State(state.missionaries, state.cannibals + 2, 'left'),
            State(state.missionaries + 1, state.cannibals + 1, 'left'),
            State(state.missionaries + 1, state.cannibals, 'left'),
            State(state.missionaries, state.cannibals + 1, 'left')
        ])
    return [child for child in children if child.is_valid()]

def dfs(current_state, goal_state, path, visited):
    if current_state == goal_state:
        return path
    visited.add(current_state)
    for next_state in successors(current_state):
        if next_state not in visited:
            new_path = dfs(next_state, goal_state, path + [next_state], visited)
            if new_path:
                return new_path
    return None

def print_solution(solution):
    for idx, state in enumerate(solution):
        print(f"Step {idx + 1}: {state.missionaries} missionaries, {state.cannibals} cannibals, boat on {state.boat} side")

if __name__ == "__main__":
    initial_state = State(3, 3, 'left')
    goal_state = State(0, 0, 'right')
    path = dfs(initial_state, goal_state, [initial_state], set())
    if path:
        print("Solution found:")
        print_solution(path)
    else:
        print("No solution found")
