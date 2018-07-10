# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:43:43 2018

@author: Chen
"""
class StackUnderflow(ValueError):
    pass

class LNode(): #栈的链表实现
    def __init__(self,elem,_next=None):
        self._elem=elem
        self._next=_next
        
class LStack():
    def __init__(self):
        self._top=None
    
    def is_empty(self):
        return self._top is None
    
    def top(self):
        if self._top is None:
            raise StackUnderflow('in LStask.tpo()')
            
        return self._top.elem
    
    def push(self,elem):
        self._top=LNode(elem,self._top)
        
    def pop(self):
        if self._top is None:
            raise StackUnderflow('in LStack.pop()')
        p=self._top
        self._top=p.next
        return p.elem
    

if __name__ == "__main__":     
    
    