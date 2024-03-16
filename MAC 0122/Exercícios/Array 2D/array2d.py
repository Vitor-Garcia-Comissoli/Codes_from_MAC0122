def main():
    
    a = Array2D( (2,3), 3)
    b = Array2D( (2,3), 4)
    
    print('a:')
    print(a) # deve imprimir
    ## 3 3 3
    ## 3 3 3
    
    print('b:')
    print(b)  # deve imprimir
    ## 4 4 4
    ## 4 4 4
    
    print('Soma com Magia (+):')
    print(a + b)
    print('Soma sem Magia:')
    print(a.add(b))
    ## 7 7 7 
    ## 7 7 7 

    print(a * 2)
    ## 6 6 6
    ## 6 6 6
    
    print(a[0,1])
    ## 3
    
    print('')
    a[1,1] = -1
    print(a)
    ## 3 3 3
    ## 3 -1 3
    
    c = Array2D( (2,2), 1)
    d = c * a
    print(d)
    
    ar = Array2D( (2,3), 5)
    print('ar: \n')
    print (ar)
    br = ar.reshape( (3,2) )
    print ('br: \n')
    print(br)
    
    br[1,1] = 99
    print('ar após alteração de br: \n')
    print(ar)
    
    print('br após alteração de br: \n')
    print(br)
    
## escreva a classe Array2D

class Array2D:
    
    def __init__ (self, shape, valor):
        
        self.shape = shape
        
        nlin, ncol = shape
        
        self.nlin = shape[0]
        self.ncol = shape[1]
        self.valor = valor
        
        size = nlin * ncol
        
        self.size = size
        self.data = [valor] * size
        
        
    def __str__ (self):
        
        s = ''
        nlin = self.nlin
        ncol = self.ncol
        
        for lin in range(nlin):
            for col in range(ncol):
                s += f'{self.data[lin * ncol + col ]}  '
            s += '\n'
        
        return s
    
    def reshape(self, novo_shape):
        
        nlin, ncol = novo_shape
        
        if self.size == nlin * ncol:
            
            novo = Array2D ((novo_shape), 0) # novo = Array2D ((0,0) , 0)
            novo.shape = novo_shape
            novo.size = self.size
            novo.data = self.data # novo.data = self.data[:]
        
            return novo
    
    def add (self, other):
        
        novo = Array2D (self.shape, 0)
        
        for i in range (self.size):
            novo.data[i] = self.data[i] + other.data[i]
        
        return novo
    
    def __add__ (self, other):
        
        novo = Array2D (self.shape, 0)
        
        for i in range (self.size):
            novo.data[i] = self.data[i] + other.data[i]
        
        return novo
        
    def __mul__ (self, other):
        
        if type(other) != int:
        
            novo = Array2D (min(self.shape, other.shape), 0)
                
            for i in range (self.size):
                novo.data[i] = self.data[i] * other.data[i]
        
        else:
            
            novo = Array2D (self.shape, 0)
            
            for i in range (self.size):
                novo.data[i] = self.data[i] * other
        
        return novo
    
    def __getitem__ (self, key):
        
        ncol = self.ncol
        
        lin, col = key
        
        return self.data[lin * ncol + col]
    
    def __setitem__ (self, key, valor):
        
        ncol = self.ncol
        
        lin, col = key
        
        self.data[lin * ncol + col] = valor
        
        return None
        
## não esqueça de chamar a main()

if __name__ == '__main__':
    main()