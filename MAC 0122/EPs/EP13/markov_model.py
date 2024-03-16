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

'''

class MarkovModel:
    
    def __init__(self, k, corpus):
        
        dicio = {}
        simb = []
        lista = []
        lista_k1 = []
        lista_k2 = []
        K = k
        
        while k <= (K+1):
            dict = {}
            for i in range(len(corpus)):
                x = i
                y = 0
                s = ''
                while y < k:
                    if x >= len(corpus):
                        x = 0
                    string = corpus[x]
                    if string not in simb:
                        simb += string
                    s += string
                    x += 1
                    y += 1
                if s not in dicio:
                    dicio[s] = 1
                    dict[s] = 1
                else:
                    dicio[s] += 1
                    dict[s] += 1
            k += 1
            
            if k == K:
                lista_k1 += sorted(list(dict.keys()))
                # print(lista_k1)

            else:
                lista_k2 += sorted(list(dict.keys()))
                # print(lista_k2)
            
        self.dicio = dicio
        self.A = len(simb)
        self.simb = sorted(simb)
        lista += lista_k1 + lista_k2
        self.lista = lista
        self.k = K
        
        '''
        print(self.dicio)
        print(self.lista)
        print(self.A)
        print(self.simb)
        '''
        
    def __str__(self):
        
        lista = self.lista
        dicio = self.dicio
        A = self.A
        k = self.k
        
        if A == 1:
            s = f'alfabeto tem {A} símbolo\n'
        else:
            s = f'alfabeto tem {A} símbolos\n'
        
        for i in range(len(dicio)):
            if i == len(dicio) - 1:
                if len(lista[i]) == k:
                    s += f'"{lista[i]}"   {dicio[lista[i]]}'
                    #s += '\n'
                else:
                    s +=f'"{lista[i]}"  {dicio[lista[i]]}'
                    #s += '\n'
            else:
                if len(lista[i]) == k:
                    s += f'"{lista[i]}"   {dicio[lista[i]]}\n'
                else:
                    s += f'"{lista[i]}"  {dicio[lista[i]]}\n'
                
        return s
        
    def alphabet(self):
        A = self.A
        simb = self.simb
        
        s = ''
        
        for i in range(A):
            s += simb[i]
        
        return s
        
    def N(self, t):
        
        dicio = self.dicio
        
        if t not in dicio:
            return 0
        else:
            return dicio[t]
        
    def laplace(self, t):
        
        A = self.A
        
        T = t[:-1]
        
        n_palc = self.N(t)
        n_pal =  self.N(T)
        
        prob = (n_palc + 0.5)/(n_pal + (A/2))
        
        return prob
        