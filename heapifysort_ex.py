def heapifyBuild(data,start,end):
    root  = start
    while True:
        child = root*2 + 1
        if child > end:
            break
        if child+1 <= end and data[child] < data[child+1]:
            child += 1
        if data[root] < data[child]:
            data[root],data[child] = data[child],data[root]
            root = child
        else:
            break
        

def heap_sort(data):
    start = len(data)//2 - 1
    end = len(data) - 1
    for i in range(start,-1,-1):
        heapifyBuild(data,i,end)
    for j in range(end,0,-1):
        data[j],data[0] = data[0],data[j]
        heapifyBuild(data,0,j-1)
    return data

if __name__ == "__main__":
    l = [3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6]
    print(heap_sort(l))

    