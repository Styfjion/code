def fun(array,n):
    if sum(array)%n:
        return -1
    mean = sum(array)//n
    for i in range(n):
        if (array[i]-mean)%2:
            return -1
    count = 0
    for i in range(n):
        if array[i] - mean>0:
            count += (array[i]-mean)//2
    return count


if __name__ == "__main__":
    n = int(input())
    array = list(map(int,input().split()))
    print(fun(array,n))


