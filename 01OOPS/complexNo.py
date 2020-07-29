class ComplexNo():

    def __init__(self, a, b):
        self.real = a
        self.complex = b
    
    def plus(self, ob):
        self.real = self.real + ob.real
        self.complex = self.complex + ob.complex
        
        self.prnt()
    
    def multiply(self, ob):
        x1 = self.real * ob.real
        x2 = self.complex * ob.complex * -1
        x = x1+x2
        
        y1 = self.real * ob.complex
        y2 = self.complex * ob.real
        y = y1+y2

        self.real = x
        self.complex = y
        
        self.prnt()
    
    def prnt(self):
        a = self.real
        b = self.complex
        
        if self.complex > 0:
            print("{} + i{}".format(a, b))
        elif self.complex < 0:
            print("{} - i{}".format(a, -1* b))
        

a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
op = int(input())

cob0 = ComplexNo(a, b)
cob1 = ComplexNo(c, d)

if op == 1:
    cob0.plus(cob1)
    
if op == 2:
    cob0.multiply(cob1)
