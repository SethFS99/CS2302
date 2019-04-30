# -*- coding: utf-8 -*-
"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath, Mali Zargaran
Lab 5
Last Edited on 4/30/2019
@author: Seth
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


def draw_maze_solved(walls,maze_rows,maze_cols,D):
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
    cur = (maze_rows*maze_cols)-1
#    print(cur)
    while (D[cur])[0] != -1:
#        print((D[cur])[0])
        if cur-(D[cur])[0] == maze_cols: #vertical line
#                print('making vertical')
                x0 = (cur%maze_cols)+.5
                x1 = x0
                y0 = (cur//maze_cols)-.5
                y1 = y0+1
        elif (D[cur])[0]-1 == cur:#horizontal line to the right
#                print('line to the right')
                x0 = ((D[cur])[0]%maze_cols)-.5
                x1 = x0+1
                y0 = (cur//maze_cols)+.5
                y1 = y0  
        elif (D[cur])[0]-maze_cols == cur:#vertical upwards
#                print('line upwards')
                x0 = ((D[cur])[0]%maze_cols)+.5
                x1 = x0
                y0 = (cur//maze_cols)+.5
                y1 = y0+1
        else:#regular horizontal
#                print('making horizontal')
                x0 = ((D[cur])[0]%maze_cols)+.5
                x1 = x0+1
                y0 = (cur//maze_cols)+.5
                y1 = y0
            
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='r')
#        print(cur)
        cur = D[cur][0]
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
def build_AL(AL, i, walls):
    #adds nodes walls[i][0] and walls[i][1] to AL and returns the new AL
    AL[(walls[i])[0]].append((walls[i])[1])
    AL[(walls[i])[1]].append((walls[i])[0])
    return AL
def breadth_first(AL):
    #array containing distance is formatted by prev. node and then distance from 0 node
    Q = []
    Q.append(0)#forsure starting point
    current = 0#Our first value in the q
    Depth = [ [] for i in range(len(AL))]
    Depth[current].append(-1)#no previous node
    Depth[current].append(0)#distance of 0
    while len(Q) != 0:
        for i in range(len(AL[current])):
            if len(Depth[(AL[current])[i]]) == 0:#if the next values have yet to be visited then add to Q
                Q.append((AL[current])[i])
                Depth[(AL[current])[i]].append(current)#lists prev node
                Depth[(AL[current])[i]].append((Depth[current])[-1]+1)#distance is 1 more than the lasts
        current = Q.pop()
        #update Q, current value, and distance value
    return Depth

def depth_first(AL):
    #array containing distance is formatted by prev. node and then distance from 0 node
    S = []
    S.append(0)#forsure starting point
    current = 0#Our first value in the q
    Depth = [ [] for i in range(len(AL))]
    Depth[current].append(-1)#no previous node
    Depth[current].append(0)#distance of 0
    while len(S) != 0:
        for i in range(len(AL[current])):
            if len(Depth[max(AL[current])]) == 0:#if the next values have yet to be visited then add to S
#                print(AL[current])
                S.append(max(AL[current]))
                Depth[max(AL[current])].append(current)#lists prev node
                Depth[max(AL[current])].append((Depth[current])[-1]+1)#distance is 1 more than the lasts
                AL[current].remove(max(AL[current]))
            elif len(Depth[min(AL[current])]) == 0:
                S.append(min(AL[current]))
                Depth[min(AL[current])].append(current)#lists prev node
                Depth[min(AL[current])].append((Depth[current])[-1]+1)#distance is 1 more than the lasts
                AL[current].remove(min(AL[current]))
#        print(S)
        current = S.pop()
        #update Q, current value, and distance value
    return Depth
    
    
    
    
    
    #creates value for the 0 node, the starting node being 0 at distance 0
plt.close("all") 
maze_rows = 15
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) #pre_maze
#constructs maze via union by size and compression
r = maze_rows*maze_cols
print('The maze has', maze_rows*maze_cols, 'cells, how many walls would you like to remove?')
r = input()
remove = int(r)
#printing output based upon user input
if remove > maze_rows*maze_cols:
    print('There is at least one path from source to destination ')
elif remove < maze_rows*maze_cols-1:
    print('A path from source to destination is not guaranteed to exist')
else:
    print('The is a unique path from source to destination ')


AL = [ [] for i in range(maze_rows*maze_cols) ] #creates an AL that has the num cells in the maze, each cell will be a node
while remove > 0: #Remove walls until there is no more walls to remove
    d = random.randint(0,len(walls)-1)
    if len(dsfToSetList(S)) == 1:#once there is a complete maze, start removing walls at random
        AL = build_AL(AL, d, walls)
        walls.pop(d)
        remove-=1
    elif find_c(S, (walls[d])[0]) != find_c(S, (walls[d])[1]):#if points are already in same set do not remove
        union_by_size(S, (walls[d])[0], (walls[d])[1])
        AL = build_AL(AL, d, walls)
        walls.pop(d)
        remove -=1

draw_maze(walls,maze_rows,maze_cols) #post_maze
print(AL)

print('##########################################################')
#print(walls)
start = time.time()
D = breadth_first(AL)
end = time.time()
print('Time for Breadth:', end - start)
S = [[] for i in range(len(AL))]
start = time.time()
S = depth_first(AL)
end = time.time()
print('Time for depth:', end - start)
#print('Using depth first')
#print(S)
print('####################################################################')
#print('using breadth first')
#print(D)

draw_maze_solved(walls,maze_rows,maze_cols, D) #post_maze

