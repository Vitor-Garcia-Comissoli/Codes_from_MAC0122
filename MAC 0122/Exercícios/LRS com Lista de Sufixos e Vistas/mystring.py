#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 7 16:37:18 2020

@author: fradim
"""
'''
Classe string que permite que fatias/substrings sejam vistas
e não clones.

Não está implementado do step em [start:stop:step]
'''
class MyString:
    def __init__(self, s, start=0, stop=None):
        self.s  = s
        self.start = start
        self.stop  = stop

        # stop máximo deve ser len(s)
        if stop == None or stop > len(s):
            self.stop = len(s)

        # s[2:2], s[3:2] deve ser MyString vazia
        if self.start >= self.stop:
            self.start = self.stop = 0

        
    def __str__(self):
        return self.s[self.start:self.stop]

    def __repr__(self):
        return f"'{self.s[self.start:self.stop]}'"
   
    def __len__(self):
        return self.stop - self.start
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.s[self.start+key]
        if isinstance(key, slice):
            if key.start is None: start = self.start 
            else: start = self.start + key.start
            if key.stop  is None: stop  = self.stop
            else: stop = self.start + key.stop
            return MyString(self.s, start, stop)
        raise TypeError(f'Índice deve ser int ou slice, e não {type(key).__name__}')

    def __lt__(self, other):
        n = min(len(self), len(other))
        s       = self.s
        s_start = self.start
        o       = other.s
        o_start = other.start 
        for i in range(n):
            if s[s_start+i] != o[o_start+i]:
                return s[s_start+i] < o[o_start+i]
        return len(self) < len(other)

    def __ge__(self, other):
        return not self < other

    def __gt__(self, other):
        n = min(len(self), len(other))
        s       = self.s
        s_start = self.start
        o       = other.s
        o_start = other.start 
        for i in range(n):
            if s[s_start+i] != o[o_start+i]:
                return s[s_start+i] > o[o_start+i]
        return len(self) < len(other)
        
    def __le__(self, other):
        return not self > other

        
    def __eq__(self, other):
        if len(self) != len(other): return False
        n = len(self)
        s       = self.s
        s_start = self.start
        o       = other.s
        o_start = other.start
        for i in range(n):
            if s[s_start+i] != o[o_start+i]:
                return False
        return True
        
    def __ne__(self, other):
        return not self == other



