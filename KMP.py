def gen_pnext(p):
    """生成pnext表，用于KMP算法 """
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m #初始元素全设为-1
    while i < m-1: #生成下一个pnext值
        if k == -1 or p[i] == p[k]:
            k,i = k+1, i+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]#当两个字符相等时要跳过
            else:
                pnext[i] = k
        else:
            k = pnext[k] #退到跟短相同前缀
    return pnext
def matching_KMP(t, p, pnext):
    """KMP串匹配，主函数"""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            j, i = j+1, i+1
        else:
            i = pnext[i]
        if i == m:
            return j-i
    return -1