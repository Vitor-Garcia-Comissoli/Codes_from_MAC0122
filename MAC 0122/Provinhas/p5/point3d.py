# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:35:51 2020

@author: vitor
"""

# from point3d import Point3D
def main():
    pos = [11, 22, 33]
    print("-------------------")
    print("Point3D.coord()")
    p0 = Point3D(pos)
    print(f"p0 = {p0}")
    pos[0] = 44
    pos_p0 = p0.coord()
    print(f"p0.coord() = {pos_p0}")
    pos_p0[0] = 55
    print(f"p0.coord() = {p0.coord()}")
    print("------------------------")
    print("Point3D + Point3D")
    p1 = Point3D()
    print(f"p1 = {p1}")
    p2 = Point3D([11, 22, 33])
    print(f"p2 = {p2}")
    print(f"p1 + p2 = {p1 + p2}")
    print("------------------------")
    print("Point3D + const")
    p3 = Point3D([44, 55, 66])
    print(f"p3 = {p3}")
    print(f"p3 + 3.5 = {p3 + 3.5}")
    print("------------------------")
    print("const + Point3D")
    p4 = Point3D([77, 88, 99])
    print(f"p4 = {p4}")
    print(f"3 + p4 = {3 + p4}")
    print("------------------------")
    print("Point3D.media()")
    p5 = Point3D([1, 1, 7])
    print(f"p5 = {p5}")
    print(f"p5.media() = {p5.media()}")
    
class Point3D:
    
    def __init__(self, lista = 3*[0]):
        
        self.list = lista[:]
        self.len = len(lista)
        self.original = lista[:]
        
    
    def __str__(self):
        
        len = self.len
        lista = self.list
        
        s = '('
        
        for i in range (len):
            if i == len-1:
                 s += f'{lista[i]}'
            else:
                s += f'{lista[i]}, '
             
        s += ')'
        
        return s
      
    def put (self, lin, valor):
        
        lista = self.list
        
        lista[lin] = valor
        
        return None
        
    def __add__(self, other):
        
        len = self.len
        lista = self.list
        
        novo = Point3D()
        
        if type(other) == int or type(other) == float:
            
            for i in range(len):
                novo[i] = lista[i] + other
                
        else:
            
            for i in range(len):
                novo[i] = lista[i] + other.list[i]
            
        return novo
    
    def __radd__ (self, other):
        
        return self + other
    
    def __setitem__ (self, chave, valor):
        
       lista = self.list
       
       lista[chave] = valor
       
       self.list = lista
        
       return None
    
    def coord(self):
        
        novo = Point3D(self.original)
        
        return novo.list
        
    def media(self):
        
        len = self.len
        lista = self.list
        soma = 0
        
        for i in range(len):
            soma += lista[i]
            
        soma = soma/3
        
        return soma
    
main()