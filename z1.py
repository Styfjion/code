class Solution:
    sum = 0
    def Go(self,steps,bufu):
        if not steps:
            self.sum += 1
            return self.sum
        else:
            for unit in bufu:
                if steps-unit >= 0:
                    self.sum += self.Go(steps-1,bufu)
        return self.sum

if __name__ == "__main__":
    #n = int(input())
    n = 13
    sum = 0
    bufu = (1,2,5,10)
    print(Solution().Go(n,bufu))
    