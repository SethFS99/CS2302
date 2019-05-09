"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath, Mali Zargaran
Lab 8
Last Edited on 5/9/2019
@author: Seth
"""
import random
import numpy as np
import math
import mpmath
from math import *

def equal(f1, f2,tries=1000,tolerance=0.000000000001):
    for i in range(tries):
        x = random.uniform(-math.pi, math.pi)#range -pi to pi
        if(f2 == 'sec(x)'):
            f2 = 'mpmath.sec(x)'
        if(f1 == 'sec(x)'):
            f1 = 'mpmath.sec(x)'
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True
def sumSet(S):
    if S == None or len(S) == 0:
        return 0
    c = 0
    for i in S:
        c+=i
    return c

def subsetsum(s1, s2,last):
#    print('set 1',s1)
#    print('set 2',s2)
    if sumSet(s1) == sumSet(s2):#found equal subsets
        return True, s1, s2
    
    if sumSet(s1)<sumSet(s2):
        if last < 0:#has gone through whole set with no possible subsets
            return False, s1, s2
        s1.append(s2[-1])#if there is more set to go through continue
        s2.remove(s2[-1])
        return False, s1, s2
    if last > len(s1) - 1:#in case no sub sets exist and returns with sets that no longer work with this portion of the code
        return False, s1, s2
    
    s2.append(s1[last])#adds s1's next element to s2 and removes it from s1
    s1.remove(s1[last])
    result, s1,s2 = subsetsum(s1,s2,last-1)
    if result:#found sub set
        return True, s1,s2
    else:
        return subsetsum(s1,s2,last-1) # Don't take S1[last]
    
FUNctions = ['sin(x)', 'cos(x)', 'tan(x)',  '-sin(x)', '-cos(x)', '-tan(x)', 'sin(-x)', 'cos(-x)', 'tan(-x)', 'sin(x) / cos(x)', '2*(sin(x/2)*cos(x/2))', 'sin(x)*sin(x)', '1 - (cos(x)*cos(x))', '(1-cos(2*x)) / 2','sec(x)', '1/cos(x)']
Found = 0
print(len(FUNctions), ' functions')
while len(FUNctions) != 0:#runs until all identities are found
    f1 = FUNctions[0]#first function to test
    FUNctions.remove(f1)#removes f1 from list to choose a non f1 function to compare
    for i in range(len(FUNctions)):
        f2 = FUNctions[i]
        if equal(f1, f2):
            print(f1, ' = ', f2)
            Found += 1
print(Found, ' identities found')
        
Set1 = [2, 4, 5, 9, 12]
Set2 = [2, 4, 5, 9, 13]
P, s1, s2 = subsetsum(Set1, [], len(Set1)-1)

if P:
    print('Set ', sorted(s1+s2), 'has a partition\n', s1, '\n', s2)
else:
    print('No partition for', s1+s2)
##test set 1 then set 2
    
    
P, s1, s2 = subsetsum(Set2, [], len(Set2)-1)

if P:
    print('Set ', sorted(s1+s2), 'has a partition\n', s1, '\n', s2)
else:
    print('No partition for', sorted(s1+s2))