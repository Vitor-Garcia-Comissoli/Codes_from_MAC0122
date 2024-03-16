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
    monitores e colegas). Com exceção de material de MAC0122, caso
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
# MarkovModel(), MarkovModel.laplace(), __str__()
from markov_model import MarkovModel

# math.log()
import math

class TopModel:
    
    def __init__(self, k, dict_corpora):
        
        self.dicio = dict_corpora
        self.k = k
        
        tam = len(dict_corpora)
        self.tam = tam
        
        self.lista_chaves = list(self.dicio.keys())
        self.lista_valores = list(self.dicio.values())
        
        lista_markov = []
        
        for i in range(tam):
            
            lista_markov += [MarkovModel(k,self.lista_valores[i])]
        
        self.lista_markov = lista_markov    
    
    def __str__(self):
      
        s = f'TopModel possui {self.tam} modelos: '
        
        for j in range(self.tam):
            if j < self.tam-1:
                s += f'{self.lista_chaves[j]},'
            else:
                s +=f'{self.lista_chaves[j]}\n'
        
        for i in range(self.tam):
            if i < self.tam-1:
                s += f'Modelo {self.lista_chaves[i]}:\n{str(self.lista_markov[i])}\n'
            else:
                s += f'Modelo {self.lista_chaves[i]}:\n{str(self.lista_markov[i])}'
        
        return s
        
    def modelo(self, nome_modelo):
        
        if nome_modelo not in self.lista_chaves:
            print(f"modelo(): modelo '{nome_modelo}' não foi definido")
            return None
        else:
            val = self.lista_chaves.index(nome_modelo)
            return self.lista_markov[val]
    
    def verossimilhanca_total(self, nome_modelo, citacao):
        
        k = self.k
        
        if nome_modelo not in self.lista_chaves:
            print(f"verossimilhanca_total(): modelo '{nome_modelo}' não foi definido")
            return None
        else:
            val = self.lista_chaves.index(nome_modelo)
            markov = self.lista_markov[val]
            
            prob = 0
            
            for i in range(len(citacao)):
                string = ''
                x = i
                for j in range(k+1):
                    if x < len(citacao): 
                        string += citacao[x]
                        x += 1
                    else:
                        x = 0
                        string += citacao[x]
                        x += 1
                        
                prob += math.log(markov.laplace(string))
            
            return prob
    
    def media_verossimilhanca(self, nome_modelo, citacao):
        
        if nome_modelo not in self.lista_chaves:
            print(f" media_verossimilhanca(): modelo '{nome_modelo}' não foi definido")
            return None
        else:
            prob = self.verossimilhanca_total(nome_modelo, citacao)
                
            return (prob/len(citacao))
                
    def top_model(self, citacao):
        
        tam = len(self.lista_chaves)
        
        maximo = self.media_verossimilhanca(self.lista_chaves[0], citacao)
        index_max = 0
        
        for i in range(tam):
            if maximo < self.media_verossimilhanca(self.lista_chaves[i], citacao):
                maximo = self.media_verossimilhanca(self.lista_chaves[i], citacao)
                index_max = i
        
        return self.lista_chaves[index_max] , maximo
            
