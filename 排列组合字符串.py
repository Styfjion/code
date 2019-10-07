def permutation(string):
    if not string:
        return ''
    if len(string) == 1:
        return string
    strList = list(string)
    strList.sort()
    pstr = []
    for i in range(len(strList)):
        if i and strList[i-1] == strList[i]:
            continue
        subList = permutation(''.join(strList[:i])+''.join(strList[i+1:]))
        for item in subList:
            pstr.append(strList[i]+item)
    return pstr

if __name__ == "__main__":
    res = permutation('1234')
    print(res)
    print(len(res))

    
