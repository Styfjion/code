if __name__ == "__main__":
    while True:
        try:
            length = int(input())
            numberList = []
            for i in range(length):
                numberList.append(int(input()))
            numberList = list(set(numberList))
            numberList.sort()
            for unit in numberList:
                print(unit)
        except:
            break
