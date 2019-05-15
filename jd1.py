def lianxv(strList):
    preNumber = 0
    i = 0
    while i<len(strList):
        if strList[i] == '1':
            for j in range(i+1,len(strList)):
                if strList[j] == '0':
                    break
            if j <= i:
                break
            if (j-i) > preNumber:
                preNumber = j-i
            i = j
        else:
            i += 1
    return preNumber
        
        