# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:01:03 2019

@author: Bianca
"""

Fizz_Buzz_list = list(range(1,101))
print(Fizz_Buzz_list)

for i in Fizz_Buzz_list:
    print(i)

for i in Fizz_Buzz_list: 
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)