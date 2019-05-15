import sys
import math
if __name__ == "__main__":
    yuwan = 1
    rouwan = 2
    wanshu = 3
    sum = 0
    result = []
    for i in range(1,wanshu):
        if rouwan < i:
            continue
        rouwanzuhe = math.factorial(rouwan-1)/(math.factorial(rouwan-i)*math.factorial(i-1))
        for j in range(1,wanshu+1-i):
            if yuwan < j:
                continue
            yuwanzuhe = math.factorial(yuwan-1)/(math.factorial(yuwan-j)*math.factorial(j-1))
            sum += rouwanzuhe*yuwanzuhe
    print(int(sum%1e4))
