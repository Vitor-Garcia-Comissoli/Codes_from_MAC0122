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
        
        Para a elaboração deste EP utilizei-me somente dos conteúdos
        lecionados em sala de aula e de EPs anteriores deste mesmo curso.

'''
import numpy as np

#-------------------------------------------------------------------------- 

def main():
    '''
    programa para testar a classe NumPymagem
    '''

    lista = []
    k = 0
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(k)  
            k += 1
        lista.append(linha)

    img1 = NumPymagem( 0, 0, np.array(lista))  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}")

    img2 = NumPymagem( 4, 3, 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}")

    print("\nChamadas do método crop")
    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}")
    
    img4 = img1.crop(1, 1, 4, 5)  
    print(f"img4:\n{img4}")
    
    img5 = img4 + img3 * 0.5
    print(f"img5:\n{img5}")

    img6 = NumPymagem( 5,5 )
    print(f"img6:\n{img6}")
    img6.paste(img5, -1, 1)
    print(f"img6 paste img5:\n{img6}")

    img7 = NumPymagem( 9, 9, 0.0)
    img8 = img7.crop()
    
    img7.pinte_disco(1.1, 7, 0, 8)
    print(f"teste disco:\n{img7}")
    
    img8.pinte_retangulo(8.8, -1, 4, 5, 8)
    print(f"teste retangulo:\n{img8}")

    print("teste disco com retangulo:")
    print(img7 + img8 * 0.5)

    ### TESTE O SEU PROGRAMA COM OUTROS EXEMPLOS
    ### PODE COLOCA-LOS NO FORUM

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem
    
    def __init__ (self, nlin, ncol, valor = 0):
        
        if type(valor) == np.ndarray: #np.array
            self.NumPymagem = valor[:]
            self.nlin = len(self.NumPymagem)
            self.ncol = len(self.NumPymagem[0])
            self.shape = (self.nlin, self.ncol)
            
        
        else:
            self.nlin = nlin
            self.ncol = ncol
            self.shape = (nlin, ncol)
            self.NumPymagem = np.full(self.shape, valor)
        
    def __str__ (self):
        
        nlin = self.nlin
        ncol = self.ncol
        NumPymagem = self.NumPymagem
        
        s = ""
        
        for i in range(0, nlin, + 1):
            for j in range(0, ncol, +1):
                
                if nlin == 1:
                    
                    if j == (ncol - 1):
                        s +=  f"{NumPymagem[j]}"
                
                    else:
                        s +=  f"{NumPymagem[j]}, "
                
                elif j == (ncol - 1):
                    s +=  f"{NumPymagem[i,j]}"
                
                else:
                    s +=  f"{NumPymagem[i,j]}, "
                
            s += "\n"

        return s
    
    def size(self):
        
        size = self.size
        return size
    
    def __getitem__(self, tupla):
        
        NumPymagem = self.NumPymagem
        nlin = self.nlin
        
        if nlin == 1:
            
            alvo = NumPymagem[tupla]
            
        else:
            
            alvo = NumPymagem[tupla]
        
        return alvo
    
    def __setitem__ (self, tupla, valor):
        
        NumPymagem = self.NumPymagem
        nlin = self.nlin
        
        if nlin == 1:
            
            NumPymagem[tupla] = valor
            
        else:
            
            NumPymagem[tupla] = valor
        
        return None
    
    def __add__ (self, other):
        
        Imagem = self.NumPymagem
        
        if type(other) == int or type(other) == float:
            
            nova = Imagem + other
            
            nova_array = NumPymagem(0, 0, nova)
            
        else:
            
            Imagem2 = other.NumPymagem
            
            a = np.array(Imagem)
            b = np.array(Imagem2)
    
            nova = a + b
            
            nova_array = NumPymagem(0, 0, nova)
            
            
        return nova_array
    
    def __radd__(self, other):
        
        return self + other
    
    def __mul__(self, other):
        
        Imagem = self.NumPymagem
    
        nova = Imagem * other
            
        nova_array = NumPymagem(0, 0, nova)
            
        return nova_array
        
    def __rmul__(self, other):
        
        return self * other
    
    def crop(self, left = 0, top = 0, right = None, bottom = None):
        
        Imagem = self.NumPymagem
        nlin = self.nlin
        ncol = self.ncol
        
        if right == None:
            right = ncol
            
        if bottom == None:
            bottom = nlin
        
        # nlin2 = (bottom - top)
        # ncol2 = (right - left)
        
        a = np.array(Imagem)
        
        # crop_array = NumPymagem(nlin2, ncol2, 0)
        
        # print(crop_array)
        
        crop = a[top : bottom, left : right]
        '''
        for i in range (nlin2):
            for j in range (ncol2):
                
                val = crop[i,j]
                crop_array[i,j] = val
        '''
        crop_array = NumPymagem(0, 0, crop)
        
        # print(type(crop_array))
        # print(crop_array)
        
        return crop_array
        
    def paste(self, other, tlin = 0, tcol = 0):
        
        Imagem = self.NumPymagem
        Imagem2 = other.NumPymagem
        
        nlin = self.nlin
        ncol = self.ncol
        
        nlin2 = other.nlin
        ncol2 = other.ncol
        
        if nlin == 0 or ncol == 0:
            
            return None
        
        elif nlin2 == 0 or ncol == 0:
            
            return None
        '''
        if nlin2 > nlin:
            nlin2 = nlin
        
        if ncol2 > ncol:
            ncol2 = ncol
        '''
        fim_lin = tlin + nlin2
        fim_col = tcol + ncol2
        
        if fim_lin > (nlin - tlin):
            fim_lin = (nlin - tlin)
        
        if fim_col > (ncol - tcol):
            fim_col = (ncol - tcol)
       
        erro_lin = 0
        erro_col = 0
        
        if tlin < 0:
            erro_lin = tlin * (-1)
            tlin = 0
            
        if tcol < 0:
            erro_col = tcol * (-1)
            tcol = 0
        
        a = erro_lin
        b = erro_col
        
        for i in range(tlin, fim_lin):
            for j in range(tcol, fim_col):
                Imagem[i,j] = Imagem2[a,b]
                b += 1
            b = erro_col
            a += 1
        
        # print(Imagem[tlin : fim_lin, tcol : fim_col])
        # print(Imagem2[erro_lin :, erro_col :])
        '''
        Imagem[tlin : fim_lin, tcol : fim_col] = Imagem2[erro_lin : nlin2, erro_col : ncol2]
        '''
        # print(Imagem)
        
        return None
    
    def pinte_disco(self, val, raio, clin, ccol):
        
        Imagem = self.NumPymagem
        nlin = self.nlin
        ncol = self.ncol
        
        for i in range(nlin):
            for j in range(ncol):
                if (clin - i)**2 + (ccol - j)**2 < raio**2:
                    Imagem[i,j] = val
                    
        return None
        
    # Equação da Circunferência  ==> (x-a)**2 + (y-b)**2 == raio**2
    
    def pinte_retangulo(self, val, left = 0, top = 0, right = None, bottom = None):
        
        Imagem = self.NumPymagem
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
        
        Imagem[top : bottom, left : right] = val
        
        return None
    
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