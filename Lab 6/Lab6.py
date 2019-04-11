"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath, Mali Zargaran
Lab 5
Last Edited on 4.11.2019
@author: Seth
Code for drawing mazes: Olac Fuentes
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

plt.close("all") 
maze_rows = 10
maze_cols = 20

walls = wall_list(maze_rows,maze_cols)
#walls is a 138 x2 matrix
# [[0,1]
# [0,15]
# [1,2]]ETC.
S = DisjointSetForest(maze_rows*maze_cols)
choice = 0
choice = input('1.Union by size with compression\n2.Normal union\nSelection: ')
if int(choice) == 2:
    print('You have selected normal union')
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) #pre_maze
    #constructs maze via normal union
    start = time.time()
    while len(dsfToSetList(S)) != 1: #Remove walls until they are all in one set
        d = random.randint(0,len(walls)-1)
        #print('removing wall ',walls[d])
        if find(S, (walls[d])[0]) != find(S, (walls[d])[1]):
            union(S, (walls[d])[0], (walls[d])[1])
            walls.pop(d)
    end = time.time()
    draw_maze(walls,maze_rows,maze_cols) #post_maze
    print('Time to create maze: ', end - start)
#    numS=dsfToSetList(S)
#    print(numS)
#    print(len(numS))
if int(choice) == 1:
    print('You have selected Union by size and compression')
    draw_maze(walls,maze_rows,maze_cols,cell_nums=True) #pre_maze
    #constructs maze via union by size and compression
    start = time.time()
    while len(dsfToSetList(S)) != 1: #Remove walls until there is only one set
        d = random.randint(0,len(walls)-1)
        #print('removing wall ',walls[d])
        if find(S, (walls[d])[0]) != find(S, (walls[d])[1]):#if points are already in same set do not remove
            union_by_size(S, (walls[d])[0], (walls[d])[1])
            walls.pop(d)
    end = time.time()
    draw_maze(walls,maze_rows,maze_cols) #post_maze
    print('Time to create maze: ', end - start)
#    numS=dsfToSetList(S)
#    print(numS)
#    print(len(numS))
