# 小数化分数
# 给一个范围,用范围内的数组成分数,并使这个分数的值最接近所给的小数(如样例给的是1-100和1-1000的范围)
# 样例输入1: 3.1415926535897 100
# 样例输出1: 22 : 7
# 1
# 2
	
# 样例输入1: 3.1415926535897 100
# 样例输出1: 22 : 7

# 样例输入2: 3.1415926535897 1000
# 样例输出2: 355 : 113
# 1
# 2
	
# 样例输入2: 3.1415926535897 1000
# 样例输出2: 355 : 113

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
import sys
if len(sys.argv)<2:
    print "Enter the num and up:",
    m = raw_input()
else:
    m = " ".join(sys.argv[1:])
m=m.split()
if len(m)<2:
    print "Input error!"
    sys.exit()
b=int(m[1])
t=eval(m[0])
a1=1
a2=1
mina1=1
mina2=1
mindt=10000
while a1<b+1 and a2<b+1:
    a3=a1*1.0/a2
    if abs(a3-t)<mindt:
        mindt=abs(a3-t)
        mina1=a1
        mina2=a2
    if a3<t:
        a1+=1
    elif a3>t:
        a2+=1
    else:
        break
a3 = gcd(mina1,mina2)
print mina1/a3,":",mina2/a3