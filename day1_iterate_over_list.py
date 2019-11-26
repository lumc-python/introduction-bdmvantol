# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:00:06 2019

@author: Bianca
"""

simple_list = list(range(0,10))
print(simple_list)

for i in simple_list:
    print(i)

for i in simple_list[::-1]:
    if i>2:
        print('{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer on the wall'.format(i,i,i-1))
    elif i>1:
        print('{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottle of beer on the wall'.format(i,i,i-1))
    elif i == 1:
        print('{} bottle of beer on the wall, {} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall'.format(i,i))
    else: 
        print('No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')