from Node import Node
import sys

class BFSsearch:
    def __init__(self,bigMaze,numDots,Pacman,row,col):
        self.maze =bigMaze
        self.solution=[]
        self.totalDots=numDots
        self.beginning=Pacman
        self.totalNodesExpanded=0
        self.maxTreeDepth=0
        self.solutionCost=0
        self.maxFrontier=0
        self.current=False
        self.extraHeads=numDots-1
    def findPathBfs(self):
        root=Node()
        root.loc=self.beginning
        self.solution.append(self.beginning)
        self.findPathbfs(root)
        del root
    def solutionAssemble(self,root):
        if root.parent==None:
            return
        self.solution.append(root.loc)
        self.solutionAssemble(root.parent)
    def findPathbfs(self,root):
        tempmaze=self.maze.copy()
        bfs=[]
        bfs.append(root)
        root=None
        last=Node()
        temp=None
        while len(bfs)>0:
            self.maxTreeDepth+=1
            size=len(bfs)
            self.maxFrontier=max(self.maxFrontier,size)
            temp=bfs.pop(0)
            x=temp.loc[0]
            y=temp.loc[1]
            #MOVE UP
            if tempmaze[x][y-1]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x][y-1]==3:
                    last.loc=[x,y-1]
                    tempmaze[x][y-1]=0
                    self.maze[x][y-1]=1
                    last.parent=temp
                    break
                tempmaze[x][y-1]=0
                node1=Node()
                node1.parent=temp
                node1.loc=[x,y-1]
                tempNode = [n for n in bfs if n.loc==node1.loc]
                if len(tempNode)==0:
                    bfs.insert(len(bfs),node1)
            #Move LEFT
            if tempmaze[x-1][y]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x-1][y]==3:
                    last.loc=[x-1,y]
                    tempmaze[x-1][y]=0
                    self.maze[x-1][y]=1
                    last.parent=temp
                    break
                tempmaze[x-1][y]=0
                node2=Node()
                node2.parent=temp
                node2.loc=[x-1,y]
                tempNode = [n for n in bfs if n.loc==node2.loc]
                if len(tempNode)==0:
                    bfs.insert(len(bfs),node2)
            #Move Down
            if tempmaze[x][y+1]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x][y+1]==3:
                    last.loc=[x,y+1]
                    tempmaze[x][y+1]=0
                    self.maze[x][y+1]=1
                    last.parent=temp
                    break
                tempmaze[x][y+1]=0
                node3=Node()
                node3.parent=temp
                node3.loc=[x,y+1]
                tempNode = [n for n in bfs if n.loc==node3.loc]
                if len(tempNode)==0:
                    bfs.insert(len(bfs),node3)
            #MOVE RIGHT
            if tempmaze[x+1][y]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x+1][y]==3:
                    last.loc=[x+1,y]
                    tempmaze[x+1][y]=0
                    self.maze[x+1][y]=1
                    last.parent=temp
                    break
                tempmaze[x+1][y]=0
                node4=Node()
                node4.parent=temp
                node4.loc=[x+1,y]
                tempNode = [n for n in bfs if n.loc==node4.loc]
                if len(tempNode)==0:
                    bfs.insert(len(bfs),node4)
        if last.parent!= None:
            self.solutionAssemble(last)
            self.totalDots-=1
            if self.totalDots>0:
                newNode = Node()
                newNode.loc = last.loc
                self.findPathbfs(newNode)
            
        del temp
        temp=None
        del last
        last=None
        while len(bfs)>0:
            temp=bfs[0]
            bfs.pop(0)
            del temp
            temp=None
    def rS(self):
        return self.solution
    def rSC(self):#Retrieve Solution Cost
        if len(self.solution)>0:
            return len(self.solution)
        else:
            return -1
    def rTD(self):#Retrieve Tree Depth
        return self.maxTreeDepth
    def rSF(self):#Retrieve Size Frontier
        return self.maxFrontier
    def __del__(self):
        del self
    def returnNodesExpand(self):
        return self.totalNodesExpanded




