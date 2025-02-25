from math import sqrt
from Node import Node


class ASTsearch:
    def __init__(self,bigMaze,numDots,Pacman,row,col,goals):
        self.maze=bigMaze
        self.totalDots=numDots
        self.beginning=Pacman
        self.solution=[]
        self.goals=goals
        self.maxTreeDepth=0
        self.maxFrontier=0

        self.t=0
    def heuristic_cost_estimate(self,lhs,rhs):
        return abs(rhs.loc[0]-lhs.loc[0])+abs(rhs.loc[1]-lhs.loc[1])
    def heuristic_cost_estimate_euclidean(self,lhs,rhs):
        return sqrt(pow(rhs.loc[0]-lhs.loc[0],2)+pow(rhs.loc[1]-lhs.loc[1],2))
    def heuristic_cost_estimate_chebyshev(self,lhs,rhs):
        return max(abs(rhs.loc[0]-lhs.loc[0]),abs(rhs.loc[1]-lhs.loc[1]))
    def findPathAst(self):
        root=Node()
        root.loc=self.beginning
        self.solution.append(self.beginning)
        self.findPathAST(root)
        del root
    def findPathAST(self,root):
        nodelist=[[0 for i in range(100)]for j in range(100)]
        tempmaze=self.maze.copy()
        for i in range(100):
            for j in range(100):
                node=Node()
                node.loc=[i,j]
                nodelist[i][j]=node
        openlist=[]
        closedlist=[]
        openlist.append(root)
        lowestFNode=None
        current=None
        while len(openlist)!=0:
            self.maxTreeDepth+=1
            size=len(openlist)
            self.maxFrontier=max(self.maxFrontier,size)
            lowestF=99999.0
            for i in openlist:
                lowestFNode=i
                if lowestFNode.f<lowestF:
                    lowestF=lowestFNode.f
                    current=lowestFNode
            if current.loc==self.goals[self.t].loc:
                self.solutionAssemble(current)
                self.t+=1
                self.totalDots-=1
                if self.totalDots>0:
                    newNode = Node()
                    newNode.loc = current.loc
                    self.findPathAST(newNode)
                self.totalNodesExpand=len(closedlist)
                return
            openlist.remove(current)
            closedlist.append(current)
            Neighbors=self.getNeighbors(tempmaze,current,nodelist)
            for i in Neighbors:
                neighbor=i
                findNieghiter=[neb for neb in closedlist if neb==i]
                if len(findNieghiter)>0:
                    found=findNieghiter[0]
                    if neighbor.loc==found.loc:
                        continue
                gval=current.g+1
                isGBest=False
                findNieghiter2 = [neb for neb in openlist if neb == neighbor]
                if len(findNieghiter2)>0:
                    foundOpen=findNieghiter2[0]
                    if neighbor.loc!=foundOpen.loc:
                        isGBest=True
                        neighbor.h=self.heuristic_cost_estimate_euclidean(neighbor,self.goals[self.t])
                        openlist.append(neighbor)
                    elif gval<neighbor.g:
                        isGBest=True
                elif len(findNieghiter2)==0:
                    isGBest=True
                    neighbor.h=self.heuristic_cost_estimate_euclidean(neighbor,self.goals[self.t])
                    openlist.append(neighbor)
                    if gval<neighbor.g:
                        isGBest=True
                if isGBest==True:
                    neighbor.parent=current
                    neighbor.g=gval
                    neighbor.f=neighbor.g+neighbor.h

    def getNeighbors(self,maze,node,nodelist):
        Nieghbors=[]
        x,y=node.loc
        #ADD UP
        if self.maze[x,y+1]!=0:
            Nieghbors.insert(0,nodelist[x][y+1])
        #ADD LEFT
        if self.maze[x-1,y]!=0:
            Nieghbors.insert(0,nodelist[x-1][y])
        #ADD DOWN
        if self.maze[x,y-1]!=0:
            Nieghbors.insert(0,nodelist[x][y-1])
        #ADD RIGHT
        if self.maze[x+1,y]!=0:
            Nieghbors.insert(0,nodelist[x+1][y])
        return Nieghbors
    def solutionAssemble(self,current):
        if current.parent==None:
            return
        self.solution.append(current.loc)
        self.solutionAssemble(current.parent)
    def rS(self):
        return self.solution
    def rSC(self):
        if len(self.solution)!=0:
            return len(self.solution)
        else:
            return-1
    def rSF(self):
        return self.maxFrontier
    def rTD(self):
        return self.maxTreeDepth
    def returnNodesExpand(self):
        return self.totalNodesExpand