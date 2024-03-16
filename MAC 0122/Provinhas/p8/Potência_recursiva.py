# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:04:50 2020

@author: vitor
"""
def main():
    print(potencia(2.5, 2))
    print(potencia(3.14, 0))

def potencia(base, expoente):
    if expoente == 0:
        return base**0
    return base * potencia(base,expoente-1)

main()