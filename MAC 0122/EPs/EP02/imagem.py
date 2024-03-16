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
        MAC0122, além das funções do EP anterior e dos exercícios realizados
        em aula.

'''

#-------------------------------------------------------------------------- 

class Imagem:
    '''
    Implementação da classe Imagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Imagem

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
        
        '''
        matriz = []
        
        for i in range(nlin2):
            lin = ncol2 * [0]
            matriz += [lin]
        '''
        
        matriz = Imagem(nlin2, ncol2)
        
        a = top
        b = left
    
        for i in range(nlin2):
            for j in range(ncol2):
                '''
                matriz[i][j] = imagem[a][b]
                '''
                matriz.put(i, j, imagem[a][b])
                b += 1
            
            b = left
            a += 1
        
        return matriz