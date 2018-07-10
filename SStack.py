# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:32:52 2018

@author: Chen
"""

class StackUnderflow(ValueError):
    pass

class SStack(): #栈的顺序表实现
    def __init__(self):
        self._elems=[]
        
    def is_empty(self):
        return self._elems==[]
    
    def top(self):
        if self._elems==[]:
            raise StackUnderflow('in SStack.top()')
            
        return self._elems[-1]
    
    def push(self, elem):
        self._elems.append(elem)
        
    def pop(self):
        if self._elems==[]:
            raise StackUnderflow('in SStack.pop')
        return self._elems.pop()

if __name__ == "__main__": 
    st1=SStack()
    st1.push(3)
    st1.push(5)
    print(st1._elems)
    while not st1.is_empty():
        print(st1.pop())
        
    list1=[1,2,3,4,5,6]
    st2=SStack()
    for x in list1:
        st1.push(x)
        
    list2=[]
    while not st1.is_empty():
        list2.append(st1.pop())
        
    print(list2)
    