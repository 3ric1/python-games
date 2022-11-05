# today we learn about Lee's algorithm
# and we'll use it to compute the path between two points, which also respectst the constraints of the maze


def lees_algorithm(start: list[int],
                   goal: list[int],
                   maze: list[list[int]]) -> list[list[int]]:
    rows, cols = len(maze), len(maze[0])
    visited = [
        [-1] * len(maze[0])
        for i in range(len(maze))
    ]

    visited[0][0] = 0
    q = [start]

    while len(q) > 0:
        curr = q.pop(0)  # q.pop(i) elimina q[i] din lista, si ti-l returneaza
        i, j = curr
        if j + 1 < cols and maze[i][j + 1] == 0 and visited[i][j + 1] == -1:
            visited[i][j + 1] = visited[i][j] + 1
            q.append([i, j + 1])
        if j - 1 >= 0 and maze[i][j - 1] == 0 and visited[i][j - 1] == -1:
            visited[i][j - 1] = visited[i][j] + 1
            q.append([i, j - 1])
        if i + 1 < rows and maze[i + 1][j] == 0 and visited[i + 1][j] == -1:
            visited[i + 1][j] = visited[i][j] + 1
            q.append([i + 1, j])
        if i - 1 >= 0 and maze[i - 1][j] == 0 and visited[i - 1][j] == -1:
            visited[i - 1][j] = visited[i][j] + 1
            q.append([i - 1, j])

    return visited


def compute_path(start: list[int],
                 goal: list[int],
                 maze: list[list[int]]):
    rows, cols = len(maze), len(maze[0])
    visited = lees_algorithm(start, goal, maze)
    i, j = goal
    path = [goal]
    while [i, j] != start:
        if j - 1 >= 0 and visited[i][j - 1] == visited[i][j] - 1:
            i, j = i, j - 1
            path.append([i, j])
            continue
        if j + 1 < cols and visited[i][j + 1] == visited[i][j] - 1:
            i, j = i, j + 1
            path.append([i, j])
            continue

        if i - 1 >= 0 and visited[i - 1][j] == visited[i][j] - 1:
            i, j = i - 1, j
            path.append([i, j])
            continue
        if i + 1 < rows and visited[i + 1][j] == visited[i][j] - 1:
            i, j = i + 1, j
            path.append([i, j])
            continue
        break
    return path[::-1]


if __name__ == '__main__':
    import pprint

    pprint.pprint(
        lees_algorithm([0, 0], [2, 2], [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ])
    )
    pprint.pprint(
        compute_path([0, 0], [2, 2], [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ])
    )
