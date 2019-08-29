'''
给定一个数字，我们按照如下规则把它翻译为字符串：
0翻译成“a”，1翻译成“b”，……，11翻译成“1”,……，25翻译成“z”。
一个数字可能有多个翻译。例如：12258有5种不同的翻译，分别是“bccfi”、“bwfi”、“bczi”、“mcfi”和“mzi”。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
'''

class Solution:
    def getTranslationCount(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number<0:
            return 0
        numberStr=str(number)

        return self.getTranslateCount(numberStr)
    
    def getTranslateCount(self,numberStr):
        length=len(numberStr)
        counts=[0]*length
        #count=0
        for i in range(length-1,-1,-1):
            count=0
            if i <length-1:
                count+=counts[i+1]
            else:
                count=1
            
            if i<length-1:
                digit1=int(numberStr[i])
                digit2=int(numberStr[i+1])
                converted=digit1*10+digit2
                if converted>=10 and converted<=25:
                    if i<length-2:
                        count+=counts[i+2]
                    else:
                        count+=1
            counts[i]=count
        return counts[0]
        

if __name__=="__main__":
    print(Solution().getTranslationCount(12258))
    print(Solution().getTranslationCount(12319))
    print(Solution().getTranslationCount(-3))
    print(Solution().getTranslationCount(0))
    print(Solution().getTranslationCount(5))