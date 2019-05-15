class Solution:
    def PrintToMaxOfDigits(self, n):
        if n <= 0:
            return
        number = ['0' for i in range(n)]
        for i in range(10):
            number[0] = str(i)
            self.PrintToMaxOfDigitsCore(number,0)
    
    def PrintToMaxOfDigitsCore(self,number,digt):
        if digt == len(number)-1:
            self.PrintNum(number)
            return
        digt += 1
        for i in range(10):
            number[digt] = str(i)
            self.PrintToMaxOfDigitsCore(number,digt)

    def PrintNum(self,number):
        for i in range(len(number)):
            if number[i] != '0':
                break
        number = number[i:]
        string = ''.join(number)
        print(string)

if __name__ == "__main__":
    Solution().PrintToMaxOfDigits(3)