# @File: maze_stack_dfs


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x, y + 1),  # 右
    lambda x, y: (x + 1, y),  # 下
    lambda x, y: (x, y - 1),  # 左
    lambda x, y: (x - 1, y),  # 上
]


# DFS depth first search
def solve_maze_with_stack(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    maze[x1][y1] = 2  # 表示已经走过的路
    while len(stack) > 0:
        cur_node = stack[-1]
        if cur_node == (x2, y2):
            print(stack)
            return True
        for d in dirs:
            next_x, next_y = d(*cur_node)
            if maze[next_x][next_y] == 0:
                stack.append((next_x, next_y))
                maze[next_x][next_y] = 2
                break
        else:
            stack.pop()
    print('无路可走')
    return False

solve_maze_with_stack(1, 1, 8, 8)