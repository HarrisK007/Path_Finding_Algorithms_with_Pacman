import sys
import numpy as np

#0-wall
#1-blank
#2-pacman
#3-dot

import BFSsearch
import ASTsearch
import UCsearch
from Node import Node

solution=[[0 for i in range(100)]for j in range(100)]
def make_pair(first=None,second=None):
    first=first
    return [first,second]
def retrieveSolution(rS):
    S=rS.copy()
    global solution
    while len(S)>0:
        x,y=S.pop()
        temp=make_pair(x,y)
        solution[temp[0]][temp[1]]=1
try:
    with open(f"{sys.argv[2]}","r") as file:
        _str=None
        row=0
        col=0
        numDots=0
        bigMaze=np.full([100,100],5,dtype="int32")
        Pacman=[]
        goals=[]
        for i in file.readlines():
            col=len(i)
            for j in range(col):
                if i[j]==" ":
                    bigMaze[row,j]=1
                elif i[j]=="P":
                    bigMaze[row,j]=2
                    Pacman=make_pair(row,j)
                elif i[j]==".":
                    bigMaze[row,j]=3
                    numDots+=1
                    newone=Node()
                    newone.loc=[row,j]
                    goals.append(newone)
                elif i[j]=="%":
                    bigMaze[row,j]=0
            row+=1
        IndexOne=sys.argv[1]
        bigMaze=bigMaze[:row,:col]
        if(IndexOne !=-1 and "bfs" in IndexOne):
            oldBigMaze = bigMaze.copy()
            my_bfs=BFSsearch.BFSsearch(bigMaze,numDots,Pacman,row,col)
            my_bfs.findPathBfs()
            retrieveSolution(my_bfs.rS())
            for i in range(row):
                for j in range(col):
                    if solution[i][j] == 1 and bigMaze[i][j] != 2:
                        bigMaze[i][j] = 3

            m1 = "-Original Maze-"
            while len(m1) < col:
                m1+=" "
            print(m1,"            ","-Solution Maze-")
            
            for i in range(row):
                for j in range(col):
                    if oldBigMaze[i][j] == 1:
                        print(" ",end="")
                    elif oldBigMaze[i][j] == 2:
                        print("P",end="")
                    elif oldBigMaze[i][j] == 3:
                        print(".",end="")
                    elif oldBigMaze[i][j] == 0:
                        print("%",end="")
                print("               ",end="")
                for j in range(col):
                    if bigMaze[i][j] == 1:
                        print(" ",end="")
                    elif bigMaze[i][j] == 2:
                        print("P",end="")
                    elif bigMaze[i][j] == 3:
                        print(".",end="")
                    elif bigMaze[i][j] == 0:
                        print("%",end="")
                print("")
            print(f"Solution Cost {my_bfs.rSC()}")
            print(f"Max Tree Depth {my_bfs.rTD()}")
            print(f"Max Frontier Size {my_bfs.rSF()}")
            print(f"Nodes Expanded {my_bfs.returnNodesExpand()}")
        elif(IndexOne !=-1 and "ast" in IndexOne):
            oldBigMaze = bigMaze.copy()
            my_ast=ASTsearch.ASTsearch(bigMaze,numDots,Pacman,row,col,goals)
            my_ast.findPathAst()
            retrieveSolution(my_ast.rS())

            for i in range(row):
                for j in range(col):
                    if (solution[i][j] == 1 and bigMaze[i][j] != 2):
                        bigMaze[i][j] = 3
            
            m1 = "-Original Maze-"
            while len(m1) < col:
                m1+=" "
            print(m1,"            ","-Solution Maze-")
            
            for i in range(row):
                for j in range(col):
                    if oldBigMaze[i][j] == 1:
                        print(" ",end="")
                    elif oldBigMaze[i][j] == 2:
                        print("P",end="")
                    elif oldBigMaze[i][j] == 3:
                        print(".",end="")
                    elif oldBigMaze[i][j] == 0:
                        print("%",end="")
                print("               ",end="")
                for j in range(col):
                    if bigMaze[i][j] == 1:
                        print(" ",end="")
                    elif bigMaze[i][j] == 2:
                        print("P",end="")
                    elif bigMaze[i][j] == 3:
                        print(".",end="")
                    elif bigMaze[i][j] == 0:
                            print("%",end="")
                print("")
            print(f"Solution Cost {my_ast.rSC()}")
            print(f"Max Tree Depth {my_ast.rTD()}")
            print(f"Max Frontier Size {my_ast.rSF()}")
            print(f"Nodes Expanded {my_ast.returnNodesExpand()}")
        elif (IndexOne != -1 and "uc" in IndexOne):
            print("Please enter a valid cost function (0,1 or 2):")
            choice = int(input("-->"))
            if choice == 1 or choice == 2 or choice==0:
                oldBigMaze = bigMaze.copy()
                my_UC = UCsearch.UniformCost(bigMaze, numDots, Pacman, row, col, goals, choice)
                my_UC.findPathUC()
                retrieveSolution(my_UC.rS())
                for i in range(row):
                    for j in range(col):
                        if solution[i][j] == 1 and bigMaze[i][j] != 2:
                            bigMaze[i][j] = 3
                
                m1 = "-Original Maze-"
                while len(m1) < col:
                    m1+=" "
                print(m1,"            ","-Solution Maze-")
                
                for i in range(row):
                    for j in range(col):
                        if oldBigMaze[i][j] == 1:
                            print(" ",end="")
                        elif oldBigMaze[i][j] == 2:
                            print("P",end="")
                        elif oldBigMaze[i][j] == 3:
                            print(".",end="")
                        elif oldBigMaze[i][j] == 0:
                            print("%",end="")
                    print("               ",end="")
                    for j in range(col):
                        if bigMaze[i][j] == 1:
                            print(" ", end="")
                        elif bigMaze[i][j] == 2:
                            print("P", end="")
                        elif bigMaze[i][j] == 3:
                            print(".", end="")
                        elif bigMaze[i][j] == 0:
                            print("%", end="")
                    print("")
                print(f"Solution Cost {my_UC.rSC()}")
                print(f"Max Tree Depth {my_UC.rTD()}")
                print(f"Max Frontier Size {my_UC.rSF()}")
                print(f"Nodes Expanded {my_UC.returnNodeExpanded()}")
        else:
            print("There is no Algorithm Named",IndexOne)
except Exception as e:
    print(e)


























