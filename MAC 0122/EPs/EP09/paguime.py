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

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''
import numpy as np

def main():
    '''(None) -> None
    programa para testar a classe Paguime
    '''

    saldo = np.array( [ [9,2], [5,2], [3,2], [2,2], [1,2] ] )
    maq = Paguime( saldo )
    print( maq )
    
    for v in range(0, 20, 3):
        pag = maq.pague(v)
        if pag is None:
            print(f"Não consegui pagar {v}")
        else:
            print(f"Paguei {v} usando:")
            print( pag )
            print( maq )
            
#------------------------------------------------------------
class Paguime:
    ''' Recebe um array com pares (fcoin, quantidade) indicando
        o tipo e quantidade disponíveis de cada fcoin e atende os 
        pagamentos quando possível.
    '''
    def __init__ (self, saldo):
        
        self.saldo = saldo
        self.len = len(saldo)
        
    def __str__ (self):
        
        saldo = self.saldo
        len = self.len
        
        s = 'O saldo da máquina é:' + '\n'
        
        for i in range(len):
            s += f'    {saldo[i,1]} fcoins de {saldo[i,0]} Frogs' + '\n'
        
        return s

    def rec (self, troco, valor):
        saldo = self.saldo
        len = self.len
        val = valor
        
        for i in range(len):
            num = saldo[i,0]
            quant = saldo[i,1]
            tro = 0
            
            while num <= val and quant > 0:
              
                val -= num
                tro += 1
                quant -= 1
                
            if val < num:   
                saldo[i,1] = quant
                troco[i][1] = tro
            
        if val > 0:
            return 0
        
        return None

    def pague (self, valor):
        
        saldo = self.saldo
        len = self.len
        
        troco = []
        
        for i in range(len):
            troco += [[saldo[i,0],0]]
        
        recursão = self.rec(troco, valor)
        
        if recursão == 0:
            return None
        
        else:
            troco_array = np.array(troco)
            return troco_array

main()       