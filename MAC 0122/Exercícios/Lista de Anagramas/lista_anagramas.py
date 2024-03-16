#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:59:18 2020

@author: fradim
"""
# para cronometrar o consumo de tempo
import time

#------------------------------------------------------------------------
def main():
    # use pt.txt ou words5.txt ou words6.txt ou pwords.txt
    nome = input("Digite o nome do arquivo: ")
    try:
        arq = open(nome, "r", encoding = "utf-8")
        print(f"lendo as palavras de {nome} ...")
        pals = arq.read()
        arq.close()
        print(f"palavras lidas...")
    except:
        print(f"Erro com o arquivo {nome}")
        return 

    # as palavras no arquivo estão separadas por ' ' ou '\n'
    print("criando lista de palavras...")
    lst_pals = pals.split()
    print(f"criada lista com {len(lst_pals)} palavras")

    # crie o dicionário de anagramas da lista de palavras
    dicio_anagramas = init_dicio_anagramas(lst_pals)
    pause()

    # exiba os anagramas
    print("lista de anagramas: ")
    for chave in dicio_anagramas:
        if len(dicio_anagramas[chave]) > 1:
            print(f"{chave}: ", end="")
            for pal in dicio_anagramas[chave]:
                print(pal, end=' ')
            print() 

#---------------------------------------------------------            
def init_dicio_anagramas(lst_pals):
    '''(list[str]) -> dict 
    RECEBE uma lista `lst_pals` de palavras.
    RETORNA um dicionário em que:
        * as CHAVES são strings com as letras ordenadas 
          de palavras  em `lst_pals` e 
        * os VALORES são as palavras que são anagramas das 
          letras na chave.
    '''         
    print("criando dicionário de anagramas...")
    inicio = time.time()
    dicio_anagramas = {}
    for pal in lst_pals:
        # letras na palavra
        paux = list(pal)

        # ordene as letras
        paux.sort()

        # crie a chave com essas letras ordenadas
        chave = ''.join(paux)

        # se a chave não está no dicionário insira
        if chave not in dicio_anagramas:   # O(1) esperado
            dicio_anagramas[chave] = set() # O(1) esperado
            # dicio_anagramas[chave] = []  # O(1) esperado
            

        # coloque a palavra no conjunto da chave    
        dicio_anagramas[chave].add(pal)      # O(1) esperado
        # dicio_anagramas[chave].append(pal) # O(1)

    fim = time.time()
    print(f"criado dicionário com {len(dicio_anagramas)} chaves")
    print(f"elapsed time = {(fim-inicio):.3f}")
    return dicio_anagramas

#------------------------------------------------------------------------
def pause():
    input("Tecle ENTER para continuar. ") 

#------------------------------------------------------------------------
if __name__ == "__main__":
    main()