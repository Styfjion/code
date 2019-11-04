class Test:
    def  __init__(self,x):
        self.var = x
        self.next = None

a  = Test(1)
b = a
b.next = Test(2)
b = b.next
print(b.var)
print(a.var)
print(a.next.var)