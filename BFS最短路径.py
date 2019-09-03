
import numpy as np
from copy import deepcopy


# 获取到各个结点的最短线路
def get_path(g):
    n = len(g)
    step = [0 for i in range(n)]  
    step_path = [[] for i in range(n)]  
    step_path[0] = [[0]]  
    q = [0]  
    while len(q) > 0:
        f = q.pop() 
        s = step[f] + 1
        for i in range(1, n):  
            if g[f][i] == 1:  
                if (step[i] == 0) or (step[i] > s):
                    step[i] = s
                    q.insert(0, i)

                    step_path[i] = deepcopy(step_path[f])
                    if len(step_path[i]) > 0:
                        for j in range(len(step_path[i])):
                            step_path[i][j].append(i)  

                elif step[i] == s:  
                    dp = deepcopy(step_path[f])
                    if len(dp) > 0:
                        for j in range(len(dp)):
                            dp[j].append(i)  
                    step_path[i] += dp

    return step_path


if __name__ == '__main__':
    
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(input()))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                beginX = i
                beginY = j
            if matrix[i][j] == 'E':
                endX = i
                endY = j

    step_path = get_path(g)
    # 输出结果
    for i in range(len(step_path)):
        size = len(step_path[i])
        print('到结点%s的最短路径%s条：' % (i, size))
        for j in range(size):
            print(step_path[i][j])