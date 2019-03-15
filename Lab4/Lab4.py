# -*- coding: utf-8 -*-
"""

"""
import math

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
def getheight(T):
    h = 0
    while T.isLeaf is not True:
        T = T.child[0]
        h +=1
    return h
def Btree_ToList(T):
    if T.isLeaf:#returns the leaf list to concatenate later
        return T.item
    NList = []#list we will return
    for i in range(len(T.child)):
        NList += Btree_ToList(T.child[i])
        if i< len(T.item):
            NList.append(T.item[i])
    return NList
def MinAtD(T, d):
    if d == 0:
        return T.item[0]
    if T.isLeaf:
        return -math.inf
    return MinAtD(T.child[0], d-1)
def MaxAtD(T, d):
    if d == 0:
        return T.item[-1]
    if T.isLeaf:
        return -math.inf
    return MaxAtD(T,d-1)

def NumNodesAtD(T, d):
    if d == 0:
        return 1
    if T.isLeaf:
        return -1
    NumNodes = 0
    for i in range(len(T.child)):
        NumNodes += NumNodesAtD(T.child[i], d-1)
    if NumNodes < 0:
        return -1
    return NumNodes
def PrintNodesAtD(T, d):
    if d == 0:
          print(T.item, end = '')
    if T.isLeaf:
        return
    for i in range(len(T.child)):
        PrintNodesAtD(T.child[i], d-1)
    
def numFullNodes(T):
    if len(T.item) == T.max_items:
        return 1
    if T.isLeaf:
        return 0
    numMax =0
    for i in range(len(T.child)):
        numMax += numFullNodes(T.child[i])
    return numMax
def numFullLeafs(T):
    if len(T.item) == T.max_items:
        if  T.isLeaf:
            return 1
        else:
            return 0
    numMax =0
    for i in range(len(T.child)):
        numMax += numFullLeafs(T.child[i])
    return numMax
def depthOfK(T, k):
    if k in T.item:
        return 0
    
    if T.isLeaf:
        return -1
    if k > T.item[-1]:
        d = depthOfK(T.child[-1], k)
        if d == -1:
            return -1
        else:
            return 1+d
    for i in range(len(T.item)):
        if k < T.item[i]:
            d = depthOfK(T.child[i], k)
            if d == 0:
                return d+1
    if d < 0:
        return -1
    return 1 + d
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6, 24, 67, 44, 125, 210, 55, 51, 41,42, 34, 39]
T = BTree()    
for i in L:
    Insert(T,i)
    

PrintD(T,'')
Print(T)
print('\n#####################################################')
print(Btree_ToList(T), '\n\n')
print(NumNodesAtD(T, 2))
PrintNodesAtD(T, 3)
print('Num full nodes: ', numFullNodes(T))

print('Num full leafs: ', numFullLeafs(T))
print('searching for item 100: ', depthOfK(T, 100))