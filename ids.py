# 8-Puzzle Problem using IDS with User Input

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def dls(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = dls(
                neighbor, goal, depth - 1, path + [neighbor]
            )

            if result is not None:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        solution = dls(start, goal, depth, [start])

        if solution is not None:
            return solution

        depth += 1


def print_puzzle(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


# Taking user input

print("Enter Initial State (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter Goal State (use 0 for blank):")
goal = tuple(map(int, input().split()))

# Check input length
if len(start) != 9 or len(goal) != 9:
    print("Error: Enter exactly 9 numbers.")

elif sorted(start) != list(range(9)) or \
     sorted(goal) != list(range(9)):
    print("Error: Enter numbers 0 to 8 exactly once.")

else:
    print("\nInitial State:")
    print_puzzle(start)

    print("Goal State:")
    print_puzzle(goal)

    # Solve using IDS
    solution = ids(start, goal)

    if solution:
        print("Solution Found!")
        print("Number of moves:", len(solution) - 1)
        print()

        for i, state in enumerate(solution):
            print("Step", i)
            print_puzzle(state)