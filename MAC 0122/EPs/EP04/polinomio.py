# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Vítor Garcia Comissoli
    NUSP: 11810411

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:
            
        Ao realizar este EP usei-me somente das habilidades trabalhadas em
        sala de aula.
'''
def main():
    # crie lista de coeficientes
    coefs = [5, 1, -2, 0, -3, 0, 0, 0, 0]

    # crie um objeto da classe Polinomio
    print("--------------------------")
    print(" 1. Polinomio.__init__()")
    p = Polinomio(coefs) # __init__()
    coefs[0] = 1000

    # exiba a lista (list) de seus coeficientes
    print("\n--------------------------")
    print(" 2. Polinomio.coeficientes()")
    pcoefs = p.coeficientes()
    print(f"coeficientes de p = {pcoefs}")
    pcoefs[0] = 1000
    print(f"coeficientes de p = {p.coeficientes()}")
    
    # exiba o polinômio
    print("\n--------------------------")
    print(" 3. Polinomio.__str__()")
    print(f"polinomio p(x) = {p}")   # __str__()

    # exiba o grau do polinômio
    print("\n--------------------------")
    print(" 4. Polinomio.grau()")
    print(f"grau de p = {p.grau()}") # grau()
    
    # crie um polinomio que represente a derivada de p
    print("\n--------------------------")
    print(" 5. Polinomio.derive()")
    dp = p.derive()  # derive()
    print(f"derivada de p é dp(x) = {dp}") # __str__() 
    ddp = dp.derive() # __derive__()
    print(f"derivada de dp é ddp(x) = {ddp}") # __str__()

    # exiba coeficiente de p, dp e ddp
    print("\n--------------------------")
    print(" 6. Polinomio.coeficientes()")
    print(f"coeficientes de   p(x) = {p.coeficientes()}")
    print(f"coeficientes de  dp(x) = {dp.coeficientes()}")
    print(f"coeficientes de ddp(x) = {ddp.coeficientes()}")
    
    # calcule o valor dos polinômios em alguns pontos
    print("\n--------------------------")
    print(" 7. Polinomio.__call__()")
    valores = [0, 1, 0.5, 3] # depois tente com complex(1,1)
    for x in valores:
        print(f"p({x}) = {p(x)},", end=" ")    # __call__() 
        print(f"dp({x}) = {dp(x)},", end=" ")  # __call__() 
        print(f"ddp({x}) = {ddp(x)}")         # __call__() 
       
    # calcule a soma de polinômios
    print("\n--------------------------")
    print(" 8. Polinomio.__add__()")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print(f"p1(x) = {p1}")
    print(f"p2(x) = {p2}")
    p3 = p1 + p2  # __add__()
    print(f"p1(x) + p2(x) = {p3}")
    p5 = p1 + 1   # __add__()
    print(f"p1(x) + 1 = {p5}")

    # calcule a soma de polinômios
    print("\n--------------------------")
    print(" 9. Polinomio.__radd__()")
    p6 = 2  + p1   # __radd__()
    print(f"2 + p1(x) = {p6}")

    # calcule a diferença de polinômios
    print("\n--------------------------")
    print("10. Polinomio.__sub__()")
    p4 = p1 - p1  # __sub__()
    print(f"p1(x) - p1(x) = {p4}")

    
    # calcule o produto de polinônios
    print("\n--------------------------")
    print("11. Polinomio.__mul__()")
    p1 = Polinomio([5, 1, -2, 0, 3])
    p2 = Polinomio([-2, 5, 1])
    print(f"p1(x) = {p1}")
    print(f"p2(x) = {p2}")
    p3 = p1 * p2   # __mul__()
    print(f"p1(x) * p2(x) = {p3}")
    p4 = p1 * p1   # __mul__()
    print(f"p1(x) * p1(x) = {p4}")
    p5 = p1 * -2   # __mul__()
    print(f"p1(x) * -2 = {p5}")

    # calcule o produto de polinônios
    print("\n--------------------------")
    print("12. Polinomio.__rmul__()")
    p6 = 3 * p1    # __rmul__()
    print(f"3 * p1(x) = {p6}")
        
#----------------------------------------------------------

class Polinomio:
    
    def __init__ (self, lista = [0]):
        
        if len(lista) == 1:
            list = lista[:]
        
        else:
            i = len(lista) - 1
        
            if lista[i] == 0 and len(lista) > 1:
                while lista[i] == 0 and i > 0:
                    i -= 1
        
            if i == -1 or i == 0:
                list = lista[:]
        
            else:
            
                list = (i+1) * ['']
        
                for j in range(0, (i + 1), 1):
                    list[j] = lista[j]
        
        self.lista = list[:]
        self.len = len(self.lista)
        
    def __str__ (self):
        
        s = ''
        c = self.lista
        len_lista = self.len
        
        for i in range (len_lista - 1, -1, -1):
            if i > 0:
                if c[i] != 0:
                    s += f'{c[i]}*x^{i} + '
            else:
                if c[i] < 0:
                    s += f'({c[i]})'
                else:
                    s += f'{c[i]}'
                
        return s
        
    def coeficientes(self):
        
        list = self.lista[:]
        return list
    
    def grau(self):
        
        len = self.len
        
        return len - 1
    
    def derive(self):
        
        lista = self.lista
        len = self.len
        
        if len == 1:
            novo = Polinomio([0])
            return novo
        
        nova = (len-1) * ['']
        
        novo = Polinomio(nova)
        
        for i in range(1 , len):
            novo.lista[i-1] = i * lista[i]
            
        # novo.lista[len-1] = 0
        
        if novo.lista == (len-1)*[0]:
                novo = Polinomio([0]) 
        
        '''
        print (self.lista)
        print (novo.lista)
        '''
        return novo
    
    def __call__(self, valor):
        
        lista = self.lista[:]
        len = self.len
        
        resultado = 0
        
        for i in range(len):
            resultado += (lista[i] * (valor**i))
        
        return resultado
    
    def __add__(self, other):
        
        lista = self.lista
        len = self.len
    
        if type(other) == int or type(other) == float:
        
            tamanho = (len*[''])
        
            novo = Polinomio(tamanho)
            
            for i in range(len):
                if type(other) == float:
                    novo.lista[i] = float(lista[i])
                else:
                    novo.lista[i] = lista[i]
                
            novo.lista[0] += other
    
        elif type(other) == Polinomio:
        
            lista_outro = other.lista
            len_outro = other.len
            
            tam = max(len, len_outro)
            minimo = min(len, len_outro)
            
            tamanho = tam * ['']
        
            novo = Polinomio(tamanho)
            
            for i in range(minimo):
                novo.lista[i] = lista[i] + lista_outro[i]
            
            if (tam - minimo) > 0:
                for i in range(minimo, tam):
                    if len > len_outro:
                        novo.lista[i] = lista[i]
                    else:
                        novo.lista[i] = lista_outro[i]
            
            if novo.lista == tam *[0]:
                novo = Polinomio([0]) 
            
            '''
            print (self.lista)
            print (other.lista)
            print (novo.lista)
            '''
        else:
            novo = None
            
        return novo
    
    def __radd__(self, other):
    
        return self + other
    
    def __sub__(self, other):
        
        lista = self.lista
        len = self.len
    
        if type(other) == int or type(other) == float:
        
            tamanho = (len*[''])
        
            novo = Polinomio(tamanho)
        
            for i in range(len):
                novo.lista[i] = lista[i]
                
            novo.lista[0] -= other
    
        else:
        
            lista_outro = other.lista
            len_outro = other.len
        
            tam = max(len, len_outro)
            minimo = min(len, len_outro)
            
            tamanho = tam * ['']
        
            novo = Polinomio(tamanho)
        
            for i in range(minimo):
                novo.lista[i] = lista[i] - lista_outro[i]
            
            if (tam - minimo) > 0:
                for i in range(minimo, tam):
                    if len > len_outro:
                        novo.lista[i] = lista[i]
                    else:
                        novo.lista[i] = (-1)*(lista_outro[i])
                        
            if novo.lista == tam *[0]:
                novo = Polinomio([0]) 
            '''
            print (self.lista)
            print (other.lista)
            print (novo.lista)
            '''
        return novo
    
    def __mul__(self, other):
        
        lista = self.lista
        len = self.len
    
        if type(other) == int or type(other) == float:
        
            tamanho = (len*[''])
        
            novo = Polinomio(tamanho)
        
            for i in range(len):
                novo.lista[i] = lista[i] * other
    
        else:
            
            lista_outro = other.lista
            len_outro = other.len
            
            tam = (len - 1) + (len_outro - 1) + 1
            
            '''
            print(tam)
            '''
            
            tamanho = tam * ['']
            
            maximo = max(len, len_outro)
            minimo = min(len, len_outro)
            
            novo = Polinomio(tamanho)
            
            if len > len_outro:
                for i in range(minimo):
                    for j in range(maximo):
                        soma = lista[j] * lista_outro[i]
                        if novo.lista[i+j] == '':
                            novo.lista[i+j] = soma
                        else:
                            novo.lista[i+j] += soma
            else:
                for i in range(minimo):
                    for j in range(maximo):
                        soma = lista[i] * lista_outro[j]
                        if novo.lista[i+j] == '':
                            novo.lista[i+j] = soma
                        else:
                            novo.lista[i+j] += soma
            '''
            print (self.lista)
            print (other.lista)
            print (novo.lista)
            '''
            
        return novo
    
    def __rmul__(self, other):
        
        return self * other
#----------------------------------------------------------

if __name__ == "__main__":
    main()
