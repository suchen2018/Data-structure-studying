# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:03:24 2018

@author: Chen
"""
from SStack import SStack

def check_parents(text): #栈的应用，括号匹配问题
    parents='()[]{}'
    open_parens='([{'
    opposite={')':'(',']':'[','}':'{'}
    
    def parentheses(text):
        i, text_len=0, len(text)
        while True:
            print(1)
            while i<text_len and text[i] not in parents:
                i+=1
                continue
            if i>=text_len:
                return
            yield text[i],i
            i+=1
                
    st=SStack()
    
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop()!=opposite[pr]:
            print('Unmatching is found at', i, 'for', pr)
            return False
        
    print('All parentheses are correctly matched.')
    return True
                
if __name__ == "__main__": 
    i='(1+1)'
    print(1)
    print(check_parents(i))
            