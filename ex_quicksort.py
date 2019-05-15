def quicksort(array):
    if len(array) >= 2:
        mid = array[len(array)//2]
        array.remove(mid)
        right,left = [],[]
        for unit in array:
            if unit>=mid:
                right.append(unit)
            else:
                left.append(unit)
        return quicksort(left)+[mid]+quicksort(right)
    else:
        return array

def megresort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = megresort(array[:mid])
    right = megresort(array[:mid])
    return mergre(left,right)

def mergre(left,right):
    r,l = 0,0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
        else:
            result.append(right[r])
    result += left[l:]
    result += right[r:]
    return result

def big_endheapy(arr,start,end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:
            break
        if child+1 < end and arr[child] < arr[child+1]:
            child += 1
        if arr[root] < arr[]

        
        
        
