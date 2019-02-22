# -*- coding: utf-8 -*-
"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath
Lab 2
Last Edited on 2.22.2019
@author: Seth
"""

#Node Functions
import random

class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        self.Len = 0
        
def IsEmpty(L):
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len +=1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.Len +=1
def Prepend(L,x):
    ##inserts x at begingin of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len+=1
    else:    
        L.head=Node(x,L.head)   
        L.Len +=1

def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
            L.Len -=1 
        else:
            L.head = L.head.next
            L.Len_=1
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
                 L.Len-=1
             else:
                 temp.next = temp.next.next
                 L.Len-=1





def BubbleS(L):
    if IsEmpty(L):
        return None
    else:
        t = L.head
        done = False
        while done != True:#runs loop until boolean variable done stays true through every comparison
            done = True
            t = L.head
            while t.next is not None:
                if t.item > t.next.item:#if current item is less than next then swap
                    nextItem = t.next.item
                    t.next.item = t.item
                    t.item = nextItem
                    done = False#if swap is made then the list is not sorted yet
                t = t.next


def QuickS(L):
    if L.Len > 1:
        pivot = L.head.item
        L1 = List()
        L2 = List()
        t = L.head.next#removes pivot from comparisons
        while t != None:
            if t.item < pivot:#sorting of items into lists less than or greater than pivot
                Append(L1, t.item)
            else:
                Append(L2, t.item)
            t = t.next
        
        QuickS(L1)#sorts list less than pivot
        QuickS(L2)#sorts list greater than pivot
        
        if IsEmpty(L1):
            Append(L1, pivot)
        else:
            Prepend(L2, pivot)
            
        if IsEmpty(L1):
            L.head = L2.head
            L.tail = L2.tail
        else:     
            L1.tail.next = L2.head#connects the left and right list
            L.head = L1.head
            L.tail = L2.tail#This line and previous connect the sorted halves to the original list
        
def MergeS(L):
    if L.Len > 1:
        L1 = List()
        L2 = List()
        t = L.head
        for i in range(L.Len //2):
            Append(L1, t.item)
            t=t.next
        while t != None:
            Append(L2, t.item)
            t = t.next
        #previous 2 loops separates L1 and L2 into halves of L
        MergeS(L1)
        MergeS(L2)
        #^ sorts split lists
        makeNewL(L)#empties L to have L1 and L2 be appending into L
        merge(L, L1, L2)
        
        
        
def merge(L,L1, L2):
    #Appends sorted Lists into L
    t1 = L1.head
    t2 = L2.head
    while t1 != None and t2 != None:
        if t1.item < t2.item:#appends T1 items
            Append(L, t1.item)
            t1 = t1.next
        else:
            Append(L, t2.item)#appends T2 items
            t2 = t2.next
    if t2 is None:
        while t1 != None:
            Append(L, t1.item)
            t1 = t1.next
    if t1 is None:
        while t2 != None:
            Append(L, t2.item)
            t2 = t2.next
    # ^ ^ for when one list t finishes and the other has remaining elements

def makeNewL(L):
    #empties all values in L so that when you merge you reuse the same list
    L.head = None
    L.tail = None
    L.Len = 0

def ModdedQuickS(L, MedPos):
    if L.Len <= 1:
        return L.head.item
    pivot = L.head.item
    L1 = List()
    L2 = List()
    t = L.head.next#removes pivot from comparisons
    while t != None:
        if t.item < pivot:#sorting of items into lists less than or greater than pivot
            Append(L1, t.item)
        else:
            Append(L2, t.item)
        t = t.next

    if L1.Len > MedPos :
        #if we know the median number is in the left list
        return ModdedQuickS(L1, MedPos)
    elif(L1.Len == 0 and MedPos == 0):#if the pivot is in the median position(In cases of if the Med position is 0 and L1 has nothing in it)
        return pivot
    elif(L1.Len == MedPos):#if the median position so happens to be the pivot
        return pivot
    else:
        return ModdedQuickS(L2, MedPos - L1.Len - 1)
        
    
    
    
def Copy(L):
    #copies list L into a new list with the same values
    copy = List()
    t = L.head
    while t != None:
        Append(copy,t.item)
        t = t.next
    return copy
            
def Median(L):
    C = Copy(L)
    BubbleS(C)
    t = C.head
    for i in range(C.Len//2):
        t = t.next
    return t.item

def Median2(L):
    C = Copy(L) 
    MergeS(C)
    t = C.head
    for i in range(C.Len//2):
        t = t.next
        
    return t.item



def Median3(L):
    C = Copy(L)
    QuickS(C)
    t = C.head
    for i in range(C.Len//2):
        t = t.next
    return t.item

def Median4(L):
    C = Copy(L)
    print(ModdedQuickS(C, C.Len//2))
    



myL = List()#creates random List of size 0 -50 with integers from 0-100
for i in range(random.randrange(50)):
    Prepend(myL, random.randrange(100))


print('Original list ', end = '')
Print(myL)#shows original list, unsorted

print('Sorted by bubble sort, median is: ', end = ' ')
print(Median(myL))
print('Sorted by merge sort, median is: ', end = ' ')
print(Median2(myL))
print('Sorted by quick sort, median is: ', end = ' ')
print(Median3(myL))
print('Sorted by modified quick sort, median is: ', end = ' ')
Median4(myL)