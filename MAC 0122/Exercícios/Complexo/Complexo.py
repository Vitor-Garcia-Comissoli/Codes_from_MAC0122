def main():
    ''' 
    Esse programa apenas testa a classe Complexo
    '''
    
    c1 = Complexo()
    print(f'c1 = {c1}')  # a saída deve ser (0+j0)

    c2 = Complexo(0,2)
    print(f'c2 = {c2}')  # a saída deve ser (2+j0)

    c3 = Complexo(3,1)
    print(f'c3 = {c3}')  # a saída deve ser (3+j1)
    
    c4 = 5.2 + c3 + c2
    print('')
    print(f'c4 = {c4}') # a saída deve ser (4+j1)
    print(f'c3 = {c3}')  # a saída deve ser (3+j1)
    
    c5 = c4 * c3
    print('')
    print(f'c5 = {c5}') # a saída deve ser (4+j1)
    print(f'c3 = {c3}')  # a saída deve ser (3+j1)
    
    print('')
    print(c5 == c4) # a saída deve ser False
    
# defina a classe
    
class Complexo:
    
    def __init__ (self, real=0, img=0):
        
        self.real = real
        self.img = img
    
    def __str__ (self):
        
        # a = float(self.real)
        # b = float(self.img)
        
        a = self.real
        b = self.img
        
        s = f'({a}+j{b})'
        
        return s
    
    def __eq__(self, other):
        
        a = self.real
        b = self.img
        
        x = other.real
        y = other.img
        
        if a == x and b == y:
            return True
        else:
            return False
    
    def __add__ (self, x):
        
        if type(x) == int or type(x) == float:
            novo_real = self.real + x
            novo_img = self.img
        else:
            novo_real = self.real + x.real
            novo_img = self.img + x.img
        
        return Complexo(novo_real, novo_img)
    
    def __radd__ (self, other):
        
        return self + other
    
    def __mul__ (self, other):
        
        if type(other) == int or type(other) == float:
            novo_real = self.real * other
            novo_img = self.img * other
        else:
            novo_real = self.real * other.real - self.img * other.img
            novo_img = self.real * other.img + self.img * other.real
            
        return Complexo(novo_real, novo_img)
    
    def __rmul__ (self, other):
        
        return self * other
        
# chame a main()
if __name__ == '__main__':
    main()