import sys
def maxTime(number,timeList):
    timeList = [int(unit) for unit in timeList]
    timeList.sort(reverse=True)
    count = 0
    chengke = timeList[:-2]
    yufu = timeList[-2:]
    while chengke:
        count += chengke.pop(0)
        count += yufu[0]
    return count

if __name__ == "__main__":
    yanglishu= int(sys.stdin.readline().strip())
    yangliList = []
    for i in range(yanglishu):
        number = int(sys.stdin.readline().strip())
        time = sys.stdin.readline().strip()
        timeList = list(map(int,time.split()))
        yangliList.append([number,time])
    for unit in yangliList:
        number = unit[0]
        timeList = unit[1]
        if len(timeList) <= 3:
            print(max(timeList))
        else:
            print(maxTime(number,timeList))
