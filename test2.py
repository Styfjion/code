class Solution:
    def Print1ToMaxOfNDigits(self, n):
        if n<=0:
            return 
        number=['0']*n
        for i in range(10):
            number[0]=str(i)
            self.Print1ToMaxOfNDigitsRecursively(number,n,0) 

    def PrintNumber(self,number):
        #此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0=True
        nLength=len(number)
        for i in range(nLength):
            if isBeginning0 and number[i]!='0':
                isBeginning0=False
            if not isBeginning0:
                print('%c' %number[i])
        print('\t')

    def Print1ToMaxOfNDigitsRecursively(self,number,length,index):
        if index==length-1:
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index+1]=str(i)
            self.Print1ToMaxOfNDigitsRecursively(number,length,index+1)

if __name__=="__main__":
    Solution().Print1ToMaxOfNDigits(2)