class Solution:
    def reOrderArray(self,array):
        if not array:
            return
        pBegin = 0
        pEnd = len(array) - 1
        while pBegin<pEnd:
            while pBegin<pEnd and array[pBegin]%2 == 1:
                pBegin += 1
            while pBegin<pEnd and array[pEnd]%2 == 0:
                pEnd -= 1
            if pBegin < pEnd:
                array[pBegin],array[pEnd] = array[pEnd],array[pBegin]
        return array

class Solution2:
    def reOrderArray(self,array):
        res1 = [i for i in array if i%2 ==1]
        res2 = [i for i in array if i%2 ==0]
        return res1+res2

if __name__ == "__main__":
    array = [1,2,3,4,5,6,7,8]
    print(Solution2().reOrderArray(array))
    