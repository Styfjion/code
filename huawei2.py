def Junior(newStr,primeStr):
    newStr = primeStr
    i = 0
    while i< len(primeStr) and primeStr[i]:
        if primeStr[i] == '(':
            if i-2:
                zimu = primeStr[i+1]
                chongfu = int(primeStr[i-1])
                oldpart = primeStr[i-1:i+3]
                newpart =  ''.join([zimu for i in range(chongfu)])
                newStr = newStr.replace(oldpart,newpart)
                i += 3
        else:
            i += 1
        return newStr

if __name__ == "__main__":
    primeStr = str(input())
    while True:
        if Junior(newStr,primeStr).find('(') >= 0:
            pass 
        else
            break
    newStr = ''.join(list(newStr)[::-1])
    print(newStr)
