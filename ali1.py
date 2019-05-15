
while(True):
    n = int(input())
    p = []
    for i in range(n):
        p.append(float(input()))
    
    p *= 100
    p = p[:100]
    
    xiaoming = [0]
    xiaohua = [0]
    for i in range(len(p)):
        temp1 = 1
        for j in range(len(xiaoming)):
            temp1 *= (1 - xiaoming[j])
        temp2 = 1
        for k in range(len(xiaohua)):
            temp2 *= (1-xiaohua[k])
        if(i % 2 == 0):
            xiaoming.append(p[i] * temp1 * temp2)
        else:
            xiaohua.append(p[i] * temp1 * temp2)
    print(sum(xiaoming), sum(xiaohua))