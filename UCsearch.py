from Node import Node


class UniformCost:
    def __init__(self,bigMaze,numDots,Pacman,row,col,goals,cF):
        self.maze=bigMaze[:row,:col]
        self.totalDots=numDots
        self.beginning=Pacman
        self.solution=[]
        self.goals=goals
        self.totalNodesExpanded=0
        self.solutionCost=0
        self.maxFrontier=0
        self.costFunct=cF
        self.maxTreeDepth=0
    def dist(self,lhs,rhs):
        x_cost=0
        tobe=0
        if self.costFunct==1:
            tobe=1/2
            x_cost=pow(tobe,abs(lhs.loc[0]-rhs.loc[0]))
        elif self.costFunct==2:
            tobe=2
            x_cost=pow(tobe,abs(lhs.loc[0]-rhs.loc[0]))
        else:
            x_cost=lhs.loc[0]-rhs.loc[0]
        if x_cost < 0:
            x_cost = -1 * x_cost
            return x_cost
        return x_cost
    def findPathUC(self):
        root=Node()
        root.loc=self.beginning
        self.solution.append(self.beginning)
        self.findPathuc(root)
    def findPathuc(self,root):
        tempmaze=self.maze.copy()
        j=0
        UC=[]
        UC.append(root)
        last=Node()
        closest=None
        temp=None
        while len(UC)>0:
            self.maxTreeDepth+=1
            size=len(UC)
            self.maxFrontier=max(self.maxFrontier,size)
            closest=UC[0]
            for i in UC:
                if self.dist(self.goals[j],closest) > self.dist(self.goals[j],i):
                    closest=i
            UC.remove(closest)
            temp=closest
            x=temp.loc[0]
            y=temp.loc[1]
            #MOVE DOWN
            if tempmaze[x+1,y]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x+1,y]==3:
                    dot=[x+1,y]
                    last.loc=dot
                    self.maze[x+1,y]=1
                    last.parent=temp
                    break
                tempmaze[x+1,y]=0
                node=Node()
                node.parent=temp
                node.loc=[x+1,y]
                UC.append(node)
            #MOVE LEFT
            if tempmaze[x,y-1]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x,y-1]==3:
                    dot=[x,y-1]
                    last.loc=dot
                    self.maze[x,y-1]=1
                    last.parent=temp
                    break
                tempmaze[x,y-1]=0
                node1=Node()
                node1.parent=temp
                node1.loc=[x,y-1]
                UC.append(node1)
            #MOVE UP
            if tempmaze[x-1,y]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x-1,y]==3:
                    dot=[x-1,y]
                    last.loc=dot
                    self.maze[x-1,y]=1
                    last.parent=temp
                    break
                tempmaze[x-1,y]=0
                node2=Node()
                node2.parent=temp
                node2.loc=[x-1,y]
                UC.append(node2)
            #MOVE RIGHT
            if tempmaze[x,y+1]!=0:
                self.totalNodesExpanded+=1
                if tempmaze[x,y+1]==3:
                    dot=[x,y+1]
                    last.loc=dot
                    self.maze[x,y+1]=1
                    last.parent=temp
                    break
                tempmaze[x,y+1]=0
                node3=Node()
                node3.parent=temp
                node3.loc=[x,y+1]
                UC.append(node3)
        if last !=None:
            self.solutionAssemble(last)
            self.totalDots-=1
            if self.totalDots>0:
                new=Node()
                new.loc=last.loc
                self.findPathuc(new)
        del temp
        del last
        del UC
    def solutionAssemble(self,root):
        if root.parent==None:
            return
        self.solution.append(root.loc)
        self.solutionAssemble(root.parent)
    def rS(self):
        return self.solution
    def rSC(self):
        if len(self.solution)>0:
            return len(self.solution)
        else:
            return -1
    def rTD(self):
        return self.maxTreeDepth
    def rSF(self):
        return self.maxFrontier
    def returnNodeExpanded(self):
        return self.totalNodesExpanded

        
