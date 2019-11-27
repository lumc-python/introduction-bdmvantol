# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:55:06 2019

@author: Bianca
"""

DNA = 'ACGT' * 3 + 'TTATT' * 5
print(DNA)
print(len(DNA))

for i in range(1, len(DNA)+1):
    print(DNA[i-1:])

for i in range(0, len(DNA)+1):
    print(DNA[i:])
    
for i in range(0,len(DNA)-2):
    print(DNA[i:i+3])
    
unique_substrings = set()
    
for i in range(0,len(DNA)-2):
    unique_substrings.add(DNA[i:i+3])

print(unique_substrings)
    
    
