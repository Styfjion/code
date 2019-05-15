class Solution:
    def ProducMax(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        product = list(range(4))
        max = 0
        for i in range(4, length+1):
            for j in range(1, int(i/2)+1):
                products = product[j]*product[i-j]
                if max < products:
                    max = products
            product.append(max)
        return product[length]


class Solution2:
    def ProducMax(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        timesOf3 = int(length/3)
        if length - timesOf3*3 == 1:
            timesOf3 -= 1
        timesOf2 = int((length-timesOf3*3)/2)
        return 3**timesOf3*2**timesOf2


if __name__ == "__main__":
    solution = Solution2()
    result = []
    for i in range(1, 11):
        result.append(solution.ProducMax(i))
    result.append(solution.ProducMax(50))
    print(result)
