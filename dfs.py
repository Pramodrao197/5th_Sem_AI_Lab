# 8-Puzzle using DFS

start = (1,2,3,4,5,6,7,8,0)

goal = (1, 2, 3,
        0, 5, 6,
        4,7, 8)


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0),
             (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal, limit=30):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if state in visited or len(path) > limit:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


def print_path(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()


path = dfs(start, goal)

if path:
    print("DFS Solution Found")
    print("Steps:", len(path) - 1)
    print_path(path)
else:
    print("Solution not found within limit")
