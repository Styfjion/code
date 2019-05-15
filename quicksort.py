import random

def partition(data,start,end):
    if not data or start<0 or end>len(data):
        raise("Invalid Input")
    index = random.randint(start,end)
    small = start - 1
    data[index],data[end] = data[end],data[index]
    for index in range(start,end):
        if data[index] < data[end]:
            small += 1
            if(small!= index):
                data[small],data[index] = data[index],data[small]
    small += 1
    data[small],data[end] = data[end],data[small]
    return small

def QuickSort(data,start,end):
    if start == end:
        return
    if start<end:
        index = partition(data,start,end)
        if index>start:
            QuickSort(data,start,index-1)
        if index<end:
            QuickSort(data,index+1,end)

if __name__ == "__main__":
    data = [3,4,9,0,0,6,8]
    QuickSort(data,0,len(data)-1)
    print(data)