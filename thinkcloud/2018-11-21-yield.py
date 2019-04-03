#!/usr/bin/env python
# -*- coding:utf-8 -*-


def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

for x in fab(7):
	print(x)

def fab_(max): 
   n, a, b = 0, 0, 1 
   while n < max: 
       print b 
       a, b = b, a + b 
       n = n + 1

fab_(7)