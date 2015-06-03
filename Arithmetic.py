class NumberError(Exception):
    pass

class natural(int):
    def __init__(self, value):
        self = abs(value)
        
    def S(self):
        return natural(int(self)+1)
    
    def __add__(self, other):
        if isinstance(other, natural):
            
            if other == 0:
               return self
            else:
                return natural(self+(other-1)).S()
            
        else:
            return(self+natural(other))

    def __mul__(self, other):
        if isinstance(other, natural):
            if other == 0:
               return 0
            else:
                return self+self*(other-1)
            
        else:
            return(self*natural(other))
        
a = natural(5)
print('a='+str(a))
b = natural(3)
print('b='+str(b))
print('a+b='+str(a+b))
print('a*b='+str(a*b))
