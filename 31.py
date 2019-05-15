class Solution:
    def IsPopOrder(self, pushV, popV):
        aux = []
        if not pushV and not popV:
            return True
        if not pushV or not popV:
            return False
        while popV:
            item = popV.pop(0)
            if aux and item == aux[-1]:
                aux.pop()
                continue
            if not item in pushV:
                return False
            while pushV[0]!= item:
                aux.append(pushV.pop(0))
            pushV.pop(0)
        return True

if __name__ == "__main__":
    print(Solution().IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
                