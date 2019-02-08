# -*- coding: utf-8 -*-
"""
Course 2302(Data Structures)
Instructor: Olac Fuentes
Teaching Assistant: Anithdita Nath
Lab 1
Last Edited on Thu, Feb  7, 2019
@author: Seth
"""

import numpy as np
import matplotlib.pyplot as plt
import math 


def draw_squares(ax,n,p,radius):#n is number of shapes drawn, p is the the size of the shape, w is where the shape's next vertexes will apear
    if n>0:
        q = p//2
        TLCorner = q - radius#creates new array where the bottom left corner is
        for i in range(len(q)):
            TLCorner[i,1] = TLCorner[i,1] + 2*radius #changes y value to move square to top right corner
        
        
        BRCorner = q + radius#creates new array for a square in top right corner
        for i in range(len(q)):
            BRCorner[i, 1] = BRCorner[i, 1] - 2*radius #changes y value to move square to bottom right corner
        
        
        ax.plot(p[:,0],p[:,1],color='k')#draws square
        
        
        draw_squares(ax, n-1, q+radius, radius)#creates top right corner
        draw_squares(ax, n-1, q-radius, radius)#creates bottom left corner
        draw_squares(ax, n-1, TLCorner, radius)#creates top left corner
        draw_squares(ax, n-1, BRCorner, radius)#creates bottom right corner
        


def draw_tree(ax, v, Dx, Dy, n):
    if n > 0:
        Node = np.array([[v[0], v[1]] , [v[0] - Dx,v[1] - Dy], [v[0], v[1]], [v[0] + Dx, v[1] - Dy]])
        #^Code above saves current vertex and the end points of the other two branches
        #by taking off how man Dx units moved to the left or right and how many Dy units down
        
        ax.plot(Node[:,0],Node[:,1] , color = 'k')#draws tree with branches
        
        vL = np.array([Node[1, 0], Node[1, 1]])#left vertex's corodinates
        vR = np.array([Node[3, 0], Node[3, 1]])#right vertex's corodinates
            
        draw_tree(ax, vL, Dx/2,Dy, n-1)#draws left node with half current Dx value to make smaller branches
        draw_tree(ax, vR, Dx/2, Dy, n-1)#draws right node with half current Dx value to make smaller branches
        
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        draw_circles(ax,n-1,[center[0]-radius/2, 0],radius*w,w)#cuts each circle in half of current radius
        
      
def draw_circles2(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
       
        draw_circles2(ax,n-1,[center[0]*w, 0],radius*w,w)#creates next circle moving the center over by w
        
def draw_circles3(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color= 'k')
        
        #the radius is cut into thirds each call to fit 3 circles across in each direction
        draw_circles3(ax,n-1,[center[0], center[1]],radius/3)#next center most circle
        
        draw_circles3(ax,n-1,[center[0] - 2*(radius/3), center[1]],radius/3)#left of center call
        draw_circles3(ax,n-1,[center[0] + 2*(radius/3), center[1]],radius/3)#right of center
        #moves center of the left circle over by 2 * radius/3  of current calls center
        #moves the center of the right circle over by 2 * radius/3 of current calls center
        
        draw_circles3(ax,n-1,[center[0], center[1] - 2*(radius/3)],radius/3)#below center
        draw_circles3(ax,n-1,[center[0], center[1] + 2*(radius/3)],radius/3)#Above center
        #moves the center of the top circle up by 2* radius/3 of current calls center
        #moves the center of the bottom circle down by 2*radius/3 of current calls center



#the following are all instances in which i call the above functions to draw the images asked of us 

plt.close("all") 
ogSize = 500
p = np.array([[-ogSize, -ogSize],[ogSize,-ogSize],[ogSize,ogSize],[-ogSize,ogSize],[-ogSize,-ogSize]])
radius = ogSize
fig, ax = plt.subplots()
draw_squares(ax,2,p,radius)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squaresA.png')



fig, ax2 = plt.subplots()
draw_squares(ax2,3,p,radius)
ax2.set_aspect(1.0)
ax2.axis('off')
plt.show()
fig.savefig('squaresB.png')

fig, ax3 = plt.subplots()
draw_squares(ax3,4,p,radius)
ax3.set_aspect(1.0)
ax3.axis('off')
plt.show()
fig.savefig('squaresC.png')

fig, ax4 = plt.subplots() 
draw_circles(ax4, 10, [100,0], 100,.5)
ax4.set_aspect(1.0)
ax4.axis('off')
plt.show()
fig.savefig('circlesA.png')


fig, ax5 = plt.subplots()
draw_circles2(ax5, 30,[100, 0], 100, .85)
ax5.set_aspect(1.0)
ax5.axis('off')
plt.show()
fig.savefig('circlesB.png')

fig, ax6 = plt.subplots()
draw_circles2(ax6, 100, [100, 0], 100, .93)
ax6.set_aspect(1.0)
ax6.axis('off')
plt.show()
fig.savefig('circlesC.png')


v = np.array([0, 0])#current vertex
fig, ax7 = plt.subplots()
draw_tree(ax7, v, 60, 100,3)
ax7.set_aspect(1.0)
ax7.axis('off')
plt.show()
fig.savefig('TreeA.png')

fig, ax8 = plt.subplots()
draw_tree(ax8, v, 60, 100,4)
ax8.set_aspect(1.0)
ax8.axis('off')
plt.show()
fig.savefig('TreeB.png')

fig, ax9 = plt.subplots()
draw_tree(ax9, v,150, 100,6)
ax9.set_aspect(1.0)
ax9.axis('off')
plt.show()
fig.savefig('TreeC.png')


fig, ax10 = plt.subplots()
draw_circles3(ax10, 3, [0, 0], 100)
ax10.set_aspect(1.0)
ax10.axis('off')
plt.show()
fig.savefig('templarA.png')

fig, ax11 = plt.subplots()
draw_circles3(ax11, 4, [0, 0], 100)
ax11.set_aspect(1.0)
ax11.axis('off')
plt.show()
fig.savefig('templarB.png')

fig, ax12 = plt.subplots()
draw_circles3(ax12, 5, [0, 0], 100)
ax12.set_aspect(1.0)
ax12.axis('off')
plt.show()
fig.savefig('templarC.png')
