N = int(raw_input())
p = []
for i in range(N):
    p.append(float(raw_input()))
p *= 100
p = p[:100]
res = [p[0]]
for i in range(2,100,2):
    tmp =1
    for j in range(i):
        tmp*=(1-p[j])
    res.append(tmp*p[i])
k = round(sum(res),4)
s = str(k)
while len(s) < 6:
    s+='0'
print(s)