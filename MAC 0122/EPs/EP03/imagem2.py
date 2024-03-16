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
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:
        
        Para fazer este EP utilizei-me dos conteúdos lecionados em MAC0110 e
        MAC0122, além dos Métodos do EP anterior e dos exercícios realizados
        em aula.
        
'''
def main():
    
    img1 = Imagem(6, 8, 200)
    img2 = Imagem(6, 8, 121)
    
    img3 = img1.crop(2, 3, 7, 6)
    print("teste crop:")
    print(img3)
    
    img2.paste(img3, 1, 2)
    print("teste paste:")
    print(img2)
    
    img4 = img1 + img2
    print("teste __add__:")
    print(img4)

    img5 = img1*0.3
    print("teste __mul__:")
    print(img5)

    img6 = img5 + img2*0.7
    print("teste __add__ e __mul__ :")
    print(img6)

    img7 = Imagem(8, 8, 2)
    img8 = img7.crop()
    
    img7.pinte_disco(0, 5, 1, 1)
    print("teste disco:")
    print(img7)
    
    img8.pinte_retangulo(8, -1, 3, 5, 6)
    print("teste retangulo:")
    print(img8)

    print("teste disco com retangulo:")
    print(img7 + img8 * 0.5)
#-------------------------------------------------------------------------- 

class Imagem:
    '''
    Implementação da classe Imagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # COPIE AQUI OS MÉTODOS DO EP02

    def __init__ (self, nlin, ncol, valor = 0):
        
        self.nlin = nlin
        self.ncol = ncol
        self.valor = valor
        
        imagem = []
    
        for i in range(nlin):
            lin = ncol * [valor]
            imagem += [lin]
        
        self.imagem = imagem
    
    def __str__ (self):
        
        nlin = self.nlin
        ncol = self.ncol
        imagem = self.imagem
        
        s = ""
        
        for i in range(0, nlin, + 1):
            for j in range(0, ncol, +1):
                
                if j == (ncol - 1):
                    s +=  f"{imagem[i][j]}"
                
                else:
                    s +=  f"{imagem[i][j]}, "
                
            s += "\n"

        return s
        
    def size (self):
        
        nlin = self.nlin
        ncol = self.ncol
        
        return(nlin, ncol)
        
    def get (self, lin, col):
        
        imagem = self.imagem
        
        alvo = imagem[lin][col]
        
        return alvo
    
    def put (self, lin, col, valor):
        
        imagem = self.imagem
        
        imagem[lin][col] = valor
        
        return None
    
    def crop (self, left = 0, top = 0, right = None, bottom = None):
        
        imagem = self.imagem
        nlin = self.nlin
        ncol = self.ncol
        
        if right == None:
            right = ncol
            
        if bottom == None:
            bottom = nlin
        
        nlin2 = (bottom - top)
        ncol2 = (right - left)
        
        matriz = Imagem(nlin2, ncol2)
        
        a = top
        b = left
    
        for i in range(nlin2):
            for j in range(ncol2):
                
                matriz.put(i, j, imagem[a][b])
                b += 1
            
            b = left
            a += 1
        
        return matriz

    # escreva aqui os NOVOS métodos da classe Imagem que fazem parte do EP03

    def __add__ (self, other):
    
        nlin = max(self.nlin, other.nlin)
        ncol = max(self.ncol, other.ncol)
    
        nova = Imagem(nlin, ncol, 0)
    
        for i in range(nlin):
            for j in range(ncol):
                val = self.imagem[i][j] + other.imagem[i][j]
                nova.put(i, j, val)
    
        return nova

    def __mul__ (self, other):
        
        nlin = self.nlin
        ncol = self.ncol
        
        nova = Imagem(nlin, ncol, 0)
        
        for i in range(nlin):
            for j in range(ncol):
                val = self.imagem[i][j] * other
                nova.put(i, j, val)
        
        return nova
    
    def paste (self, other, tlin, tcol):
        
        nlin = self.nlin
        ncol = self.ncol
        img1 = self.imagem
        
        nlin2 = other.nlin
        ncol2 = other.ncol
        
        lenlin2 = tlin + nlin2
        lencol2 = tcol + ncol2
        
        if lenlin2 > nlin:
            lenlin2 = nlin
        
        if lencol2 > ncol:
            lencol2 = ncol
        
        a = 0
        b = 0
        
        for i in range(tlin, lenlin2):
            for j in range(tcol, lencol2):
                img1[i][j] = other.imagem[a][b]
                b += 1
            b = 0
            a += 1
        
    def pinte_disco (self, val, raio, clin, ccol):
        
        imagem = self.imagem
        nlin = self.nlin
        ncol = self.ncol
        
        for i in range(nlin):
            for j in range(ncol):
                if (clin - i)**2 + (ccol - j)**2 < raio**2:
                    imagem[i][j] = val
        
        # Equação da Circunferência  ==> (x-a)**2 + (y-b)**2 == raio**2
             
    def pinte_retangulo (self, val, left = 0, top = 0, right = None, bottom = None):
        
        imagem = self.imagem
        nlin = self.nlin
        ncol = self.ncol
        
        if right == None:
            right = ncol
            
        if bottom == None:
            bottom = nlin
        
        if left < 0:
            left = 0
            
        if top < 0:
            top = 0
        
        nlin2 = (bottom - top)
        ncol2 = (right - left)
        
        a = top
        b = left
        
        for i in range(nlin2):
            for j in range(ncol2):
                imagem[a][b] = val
                b += 1
            b = left
            a += 1
        
#-------------------------------------------------------------------------- 
    
if __name__ == '__main__':
    main()