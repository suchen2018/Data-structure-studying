# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:04:12 2018

@author: Chen
"""

def knap_rec(weight, wlist, n):
    if weight==0:
        return True
    if weight<0 or (weight>0 and n<1):
        return False
    if knap_rec(weight-wlist[n-1],wlist,n-1):
        print('Item '+str(n)+':',wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False
    
if __name__=='__main__':
    a=10
    b=[1,2,3,4,2]
    n=5
    print(knap_rec(a,b,n))