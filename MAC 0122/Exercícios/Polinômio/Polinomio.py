def main():
    # crie lista de coeficientes
    coefs = [5, 1, 2, 0, 3]

    # crie um objeto da classe polinomio
    p = Polinomio(coefs) # __init__() 
    print("Polinomio p:", p) # __str__()
    # na saída deve aparecer: 5*(x^0) + 1*(x^1) + 2*(x^2) + ...
    
    coefs[2] = -10
    print('coefs: ', coefs)
    print('Polinomio p:', p)
    
# escreva a classe Polinomio
    
class Polinomio():
    
    def __init__ (self, coefs):
        
        self.coefs = coefs[:]
                 
    def __str__ (self):
        
        s = ''
        c = self.coefs
        
        for i in range (len(self.coefs)):
            if i > 0:
                s += f' + {c[i]} * x^{i}'
            else:
                s += f'{c[i]} * x^{i}'
        
        return s
# não se esqueça de chamar a main() para testar a classe
        
if __name__ == '__main__':
    main()