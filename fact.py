# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:30:27 2018

@author: Chen
"""
from SStack import SStack

def fact(n): #阶乘
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
def norec_fact(n):
    res=1
    st=SStack()
    while n>0:
        st.push(n)
        n-=1
    while not st.is_empty():
        res*=st.pop()
        
    return res