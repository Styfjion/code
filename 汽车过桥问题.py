'''
有N辆车陆续通过一座最大承重为W的桥，其中第i辆车的重量为w[i]，通过桥的时间为
t[i]。要求：第i辆车上桥的时间不早于第i-1辆车的时间;
任意时刻桥上所有车辆的总重量不超过W。
那么所有车辆通过桥所需的最短时间是多少？

输入：
第一行输入两个整数N、W（1<= N、W<= 10000）。第二行输入N个整数w[1]w[N]
（1<=w[i]<=W)。第三行输入N个整数t[1]到t[N]。（1<=t[i]<=10000)。
输出：
输出一个整数，表示所有车辆通过桥所需的最短时间。
样例输入：
4 2 
1 1 1 1
2 1 2 2
样例输出：
4
提示：
样例解释
不妨设第1辆车在0时刻上桥，则：
第2辆车也可以在0时刻上桥；
第2辆车在1时刻下桥，此时第3辆车上桥；
第1辆车在2时刻下桥，此时第4辆车上桥；
第3辆车在3时刻下桥；
第4辆车在4时刻下桥，此时所有车辆都通过桥。
'''
def fun(N,W,w,t):
    cur = []
    i = 0
    res = 0
    while i<N:
        if not cur:
            cur.append([w[i],t[i]])
            i += 1
        else:
            sumW = sum([unit[0] for unit in cur])
            if sumW+w[i] <= W:
                cur.append([w[i],t[i]])
                i += 1
                continue
            tmin = min([unit[1] for unit in cur])
            res += tmin
            index = set()
            for k,unit in enumerate(cur):
                unit[1] -= tmin
                if not unit[1]:
                    index.add(k)
            cur = [cur[j] for j in range(len(cur)) if j not in index]
    tmax = max([unit[1] for unit in cur])
    res += tmax
    return res


if __name__ == "__main__":
    N,W = map(int,input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))
    time = fun(N,W,w,t)
    print(time)