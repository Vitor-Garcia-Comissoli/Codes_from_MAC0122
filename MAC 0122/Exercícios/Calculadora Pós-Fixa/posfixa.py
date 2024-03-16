# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 08:39:34 2020

@author: Vítor Garcia Comissoli
"""

PROMPT = '>>> '

OPERADORES = '+-*/**'
ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'
ELEVADO = '**'

def main():
    
    print('Digite uma expressão pósfixa')
    print('Tenha o cuidado de separar os termos com um espaço')
    
    exp = input(PROMPT).split()
    
    res = valor_expressao(exp)
    print(f'resultado: {res} = {exp}')
    
def valor_expressao(exp):
    
    pilha = [] # Stack ()
    
    for item in exp:
        if item in OPERADORES:
            
            if len(pilha) < 2:
                
                print('ERRO: faltam operandos')
                return None
            
            v2 = pilha.pop()
            v1 = pilha.pop()
            
            if item == ADD:
                
                valor = v1 + v2
                
            elif item == SUB:
                
                valor = v1 - v2
                
            elif item == MUL:
                
                valor = v1 * v2
            
            elif item == DIV:
              
                valor = v1 / v2   
            
            elif item == ELEVADO:
            
                valor = v1 ** v2
                
        else: # operando
            if '.' in item:
                valor = float(item)
                
            else:
                valor = int(item)
            
        pilha.append(valor) # push()
    
    if len(pilha) == 0:
        return 0
    
    elif len(pilha) > 1:
        print('ERRO: faltam operadores')
        return None
    
    resultado = pilha.pop()
    return resultado

main()