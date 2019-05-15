if __name__ == "__main__":
    inputList = input().strip().split()
    number = int(inputList[0])
    strList = list(map(str,inputList[1:]))
    result = []
    for unit in strList:
        if len(unit) < 8:
            unit += ''.join(['0' for i in range(8-len(unit))])
            result.append(unit)
        else:
            numEight = int(len(unit)/8)
            for i in range(1,numEight+1):
                result.append(unit[(i-1)*8:i*8])
            if len(unit) - 8*numEight:
                res = unit[8*numEight:] + ''.join(['0' for i in range((numEight+1)*8-len(unit))])
                result.append(res)
    result.sort()
    for unit in result:
        print(unit,end=' ')

        