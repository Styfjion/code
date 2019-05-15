InvalidInput = False
class Solution:
    def Power(self, base, exponent):
        # write code here
        if abs(base-0) < 1e-6 and exponent < 0:
            global InvalidInput
            InvalidInput = True
            return 0
        result = self.PowerNoSign(base, abs(exponent))
        if exponent < 0:
            result = 1.0 / result
        return result
    
    def PowerNoSign(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        result = self.PowerNoSign(base,exponent>>1)
        result *= result
        if result & 0x1:
            result *= base
        return result
        
