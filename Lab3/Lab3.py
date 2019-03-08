import numpy as np
import matplotlib.pyplot as plt
import math 


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
def IterativeSearch(T, k):
    while T != None:
        if T.item == k:
            print('Item', k, 'found')
            return T
        if k >T.item:
            T = T.right
        else:
            T = T.left
    print('Item', k ,'not found')
    return None
def BuildBalancedT(T, A):
    if len(A) == 0:
        return None
    if len(A) == 1:
        T.item = A[0]
        return T
    if len(A) == 2:
        T.item = A[0]
        if A[1] > T.item:
            T.right = BST(A[1])
        else:
            T.left = BST(A)[1]
        return T
    mid = len(A)//2
    T.item = A[mid]
    T.left = BST(A)
    T.right = BST(A)
    T.left = BuildBalancedT(T.left, A[:mid])
    T.right = BuildBalancedT(T.right, A[mid+1:])
    return T
def TreeToList(T):
    if T == None:
        return []
    A = []
    L = [T.item]
    A = A + TreeToList(T.left)
    A = A + L
    A = A + TreeToList(T.right)
    return A
def PrintAtDepth(T, d):
    if T is None:
        return True
    if d == 0:
        print(T.item, end = ' ')
        return False
    Check1= True
    Check2= True#Check 1 and 2 are made to make sure that the loop this function is in runs 1 more than the depth of the whole tree to print it all
    Check1= PrintAtDepth(T.left, d-1)
    Check2= PrintAtDepth(T.right, d-1)
    if Check1 is False or Check2 is False:#if either is false then it runs one more time
        return False
    return Check1


def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
def draw_circles(ax,center,radius):
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        #cuts each circle in half of current radius
def draw_tree(ax, v, Dx, Dy, radius, nextCenter, T):
    if T is not None:
        Lbranch = np.array([[v[0]- radius /2 , v[1] -radius *.87 ] , [v[0] - Dx ,v[1] - Dy], [v[0]- radius/2, v[1] - radius * .87 ]])
        Rbranch = np.array([[v[0] + radius / 2, v[1] - radius *.87], [v[0] + Dx , v[1] - Dy],[v[0] + radius/2, v[1]- radius * .87]])
        #^Code above saves current vertex and the end points of the other two branches by taking off how man Dx units moved to the left or right and how many Dy units down


        if T.left != None:
            ax.plot(Lbranch[:,0],Lbranch[:,1] , color = 'k')#draws left branches if a node exists
        if T.right != None:
            ax.plot(Rbranch[:,0],Rbranch[:,1] , color = 'k')#draws right branches if a node exists next
        
        
        
        draw_circles(ax,[v[0] , nextCenter[1]],radius)#draws node
        nextCenter = [v[0], v[1]- radius - Dy]
        s = str(T.item)
        ax.text(v[0]- radius *.6,v[1] - radius *.2, s , fontdict = None, withdash = False)#prints T.item inside circles, the movement of x y values were found through experimentation of what visually looked most centered
        
        
        vL = np.array([Lbranch[1, 0], Lbranch[1, 1] - radius])#left vertex's corodinates
        vR = np.array([Rbranch[1, 0], Rbranch[1, 1] - radius])#right vertex's corodinates
        if T.left != None:
            draw_tree(ax, vL, Dx/2,Dy, radius, nextCenter, T.left)#draws left node with half current Dx value to make smaller branches
        if T.right != None:
            draw_tree(ax, vR, Dx/2, Dy, radius, nextCenter, T.right)#draws right node with half current Dx value to make smaller branches



# Code to test the functions above
T = None
A = [10,4,15,2,8,12,18,1,3,5,9,7, 13, 40, 41, 45, 11, 14]
for a in A:
    T = Insert(T,a)

plt.close('all')
v = np.array([0,0])
r = 20
nC = [0,0]
fig, ax = plt.subplots()
draw_tree(ax, v, 150, 90, r, nC, T)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('BST.png')
# ^^ question 1
IterativeSearch(T, A[4])
IterativeSearch(T, 42)
#^^ question 2
list.sort(A)
test = BuildBalancedT(BST(A), A)
#^^ question 3

v = np.array([0,0])
r = 20
nC = [0,0]
fig, ax2 = plt.subplots()
draw_tree(ax2, v, 150, 90, r, nC, test)
ax2.set_aspect(1.0)
ax2.axis('off')
plt.show()
fig.savefig('BST2.png')
#^^ Prints question 3's Tree

B = TreeToList(T)
print('Printing list B made from tree T')
print(B)
#^^ question 4

done = False
i = 0
print('Printing keys at depth in list T')
while done != True:#loops function to print keys at depth i
    done = True
    print('Keys at depth', i,':', end = ' ')
    done = PrintAtDepth(T, i)
    print()
    i +=1
done = False
i = 0

# ^^ question 5
print("Question 1's tree is figure 1, Question 2's tree is figure 2")
