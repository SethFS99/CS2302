2# -*- coding: utf-8 -*-
"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath, Mali Zargaran
Lab 5
Last Edited on 4.1.2019
@author: Seth
"""

# Implementation of hash tables with chaining using strings
import numpy as np
import time
import sys
import math

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size, num_items = 0):  
        self.item = []
        self.num_items = num_items
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # l must be the following np list of data following k
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = Hash(k,len(H.item))#only str in used in hashing process, before hashing check if a non letter char is in the str
    H.item[b].append([k,l]) 
    H.num_items += 1
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = Hash(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:#checks str
            return b, i, H.item[b][i][1]#Returns bucket b, index i, then embedding
    return b, -1, -1
 
def Hash(s,n):
    r = 0
    #must type cast s to str otherwise errors ocurr......idk why
    for c in str(s):
        r += (r*len(str(s)) + ord(c))
    return r%n


def ResizeTable(H):
    #resizes old table into a new larger table
    newTable = HashTableC(2*len(H.item) + 1)
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            #H.item[i] is the inital index of where an item is in the list, [j] is for each item in that subsequent list, [0] is to specifically acess the string portion of that list
            InsertC(newTable, ((H.item[i])[j])[0], ((H.item[i])[j])[1])
    return newTable
def CheckStr(a):
    #checks if str a is a valid string to insert
    if a.isalpha():
        return True
    return False

def Array_to_Float(array):
    #converts array of str into a float array
    embed = []
    for i in array:
        embed.append(float(i))
    return embed


def similarityH(H,b0,b1, w0, w1):#H table, B is index of list containing word 0 and 1, w0 w1 are index of the words
    DotProduct = []
    MagE0 = 0
    MagE1 = 0
    DP = 0
    
    for i in range(49):#we know that the index is 50 long
        DotProduct.append((((H.item[b0])[w0])[1])[i] * (((H.item[b1])[w1])[1])[i])
    for i in range(len(DotProduct)):
        DP += DotProduct[i]
    # ^^ calculates dotproduct
    for i in range(len((((H.item[b0])[w0])[1]))-1):
        MagE0 += (((H.item[b0])[w0])[1])[i] * (((H.item[b0])[w0])[1])[i]
    for i in range(len((((H.item[b1])[w1])[1]))-1):
        MagE1 += (((H.item[b1])[w1])[1])[i] * (((H.item[b1])[w1])[1])[i]
    MagE0 = math.sqrt(MagE0)
    MagE1 = math.sqrt(MagE1)
    # ^^ calculates magnitude of E0 and E1 
    return DP / (MagE0*MagE1)#formula for similarity 
       
def Compare_Words(H):
    try:
        f = open('Pairs.txt')
        Lines = f.readlines()
        for i in range(len(Lines)):
            temp = Lines[i].split(' ')
            print(temp)
            b0, w0, e0 = FindC(H, str(temp[0]))
            if i < len(Lines) -1 :#if else statement does the if except the last line where it does the else
                b1, w1, e1 = FindC(H, str(temp[1])[:-1])#[-2] removes the last character in str the \n
            else:
                b1, w1, e1 = FindC(H, str(temp[1]))
#            print(b1, ' : ', w1)
#            print(((H.item[b0])[w0])[0], end = ' ')
#            print(((H.item[b1])[w1])[0])
            print("%.5f" % similarityH(H, b0,b1,w0,w1))
    except:
        print('word pairs not found')
    f.close()
def PercentageEmpty(H):
    numEmpty = 0
    for i in H.item:
        if len(i) == 0:
            numEmpty+=1
    print(numEmpty)
    return (numEmpty / len(H.item)) * 100
def HashFile(H):
    try:
        f = open('glove.6B.50d.txt',encoding='utf-8')    
        Lines = f.readlines()
        for i in range(len(Lines)):
            temp = Lines[i].split(' ')#splits lines of text into arrays, [0] index will be the str, everything else will be the encoding numbers
            embedding = Array_to_Float(temp[1:])#converts rest of line into a array
    #        print(embedding)
    #        print(len(embedding))
            valid = CheckStr(temp[0])
            if valid:
                InsertC(H, str(temp[0]), embedding)
                #if the str if valid then insert str and it's embedding into hash table
            if H.num_items == len(H.item):#LF becomes 1
    #            print('Resizing from ', len(H.item))
                H = ResizeTable(H)
#        H = Re_Hash_All(H)
        f.close()
        return H
    except:
        print("ERROR 404 file is ded")

class BST(object):
    # Constructor
    def __init__(self, item,numNodes = 0, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        self.numNodes = numNodes

def Insert(T,newItem):
    if T == None:
        T = BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T
def BSTFile():
    try:
        f = open('glove.6B.50d.txt',encoding='utf-8')    
        Lines = f.readlines()
        for i in range(len(Lines)):
            temp = Lines[i].split(' ')
            embedding = Array_To_Float(temp[1:])
            if i == 0:
                T = BST([str(temp[0]), embedding])
                T.numNodes+=1
            if str(temp[0]).isalpha():
                Insert(T, [str(temp[0]), embedding])
                T.numNodes+=1
        f.close()
        return T
    except:
        print('file not found')
        sys.exit()
def Array_To_Float(array):
    #converts array of str into a float array
    embed = []
    for i in array:
        embed.append(float(i))
    return embed
def Compare_WordsBST(T):
    try:
        f = open('Pairs.txt')
        Lines = f.readlines()
        for i in range(len(Lines)):
            temp = Lines[i].split(' ')
            print(temp)
            W0 = Find(T, (temp[0]))
            if i < len(Lines)-1 :#if else statement does the if except the last line where it does the else
                W1 = Find(T, (temp[1])[:-1])#[-1] removes the last character in str the \n
            else:
                W1 = Find(T, (temp[1]))
#            print(W0.item)
#            print(W1.item)
            print("%.5f" % similarityBST(W0, W1))
    except:
        print('file not found')
        f.close()
def similarityBST(W0, W1):#W0, W1 adresses of W0 and W1 in BST
    DotProduct = []
    MagE0 = 0
    MagE1 = 0
    DP = 0
    
    for i in range(49):#we know that the index is 50 long
        DotProduct.append((W0.item[1])[i] * (W1.item[1])[i])
    for i in range(len(DotProduct)):
        DP += DotProduct[i]
    # ^^ calculates dotproduct
    for i in range(len(W0.item[1])-1):
        MagE0 += math.pow((W0.item[1])[i], 2)
        MagE1 += math.pow((W1.item[1])[i], 2)
    MagE0 = math.sqrt(MagE0)
    MagE1 = math.sqrt(MagE1)
    # ^^ calculates magnitude of E0 and E1 
    return DP / (MagE0*MagE1)#formula for similarity
def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or str(T.item[0]) == str(k):
        return T
    if str(T.item[0])<str(k):
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindDepth(T):
    if T is None:
        return 0
    Ltree = 1
    Rtree = 1
    #initialized to 1 to include their depth
    Ltree+=FindDepth(T.left)
    Rtree+=FindDepth(T.right)
    if Ltree < Rtree:
        return 1+Rtree#add root when returning
    else:
        return 1+Ltree

print('Type 1 for BST or type 2 for a Hash Table with Chaining')
choice = input("Choice: ")
if int(choice) == 1:
    print('creating BST')
    start = time.time()
    T = BSTFile()
    end = time.time()
    print('Number of nodes: ', T.numNodes)
    print('Time needed to create tree:',end-start )
    print('Height of tree: ', FindDepth(T))
    print('\n\nREADING FILE TO COMPARE WORDS.....\n\n')
#    print(T.left.left.item)
#    print(T.right.item)
#    print(T.left.right.item)
    Compare_WordsBST(T)
#sys.exit('END OF PROGRAM')
if int(choice) == 2:
    print('You chose to hash')
  
    H = HashTableC(97)#we start with 97 as it's the largest prime number from 0 -100 and we will need space
    start = time.time()
    H = HashFile(H)
    end = time.time()
    LF =  H.num_items / len(H.item)#load factor
        #print((H.item[97])[3])
        #print((H.item[97])[0])
    print('Initial table size: 97')
    print('Final table size:', len(H.item))
    print('Number of items in Table: ', H.num_items)
    print('Load factor: ', LF)
    print('Percentage of empty lists: ', PercentageEmpty(H))
    print('Time to build table: ', end - start)
    print('\n\nReading file to compare words.......\n\n')

    Compare_Words(H)
#    sys.exit('END OF PROGRAM')