# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:51:43 2018

@author: Chen
"""
from SStack import SStack

def suffix_exp_evaluator(line): #将str转化为list
    return suf_exp_evaluator(line.split())

class ESStack(SStack): #检查栈的深度
    def depth(self):
        return len(self._elems)
    
def suf_exp_evaluator(exp):
    operators='+-*/'
    st=ESStack()
    
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        
        if st.depth()<2:
            raise SyntaxError('Short of operand(s).')
        a=st.pop
        b=st.pop
        
        if x=='+':
            c=a+b
        elif x=='-':
            c=a-b
        elif x=='*':
            c=a*b
        elif x=='/':
            c=a/b
        else:
            break
        
        st.push(c)
        
    if st.depth==1:
        return st.pop()
    raise SyntaxError('Extra operand(s).')
    
def suffix_exp_calculator(): #交互式的驱动函数（主函数）
    while True:
        try:
            line=input('Suffix Expression: ')
            if line == 'end': return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print('Error: ', type(ex), ex.args)
            