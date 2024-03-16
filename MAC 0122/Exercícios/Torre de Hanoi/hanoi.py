# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:35:01 2020

@author: vitor
"""

def main():
    
    n = int(input('Digite o n: '))
    hanoi (n, 'A', 'B', 'C')
    
def hanoi(n, orig, aux, dest):
        
    if n == 0: # base
        return 
        
    hanoi(n-1, orig, dest, aux)
    print(f'mova {n} de {orig} para {dest}')
    hanoi(n-1, aux, orig, dest)
        
main()