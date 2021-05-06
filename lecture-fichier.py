import pandas as pd 
import os
df_nodes_nice=pd.read_csv(os.path.join("nice","nodes.csv"), sep=";")
df_nodes_paris=pd.read_csv(os.path.join("paris","nodes.csv"), sep=";")
","nodes.csv"), sep=";")
df_distance_nice=pd.read_csv(os.path.join("nice","distances.csv"), sep=";")
df_distance_paris=pd.read_csv(os.path.join("paris","distances.csv"), sep=";")
df_distance_grenoble=pd.read_csv(os.path.join("grenoble","distances.csv"), sep=";")
def ville():
    
<<<<<<< HEAD
 
class Reseau(object):
    def __init__(self, list_nodes, distribution):
        assert len(list_nodes)<=30
        assert df_nodes.iloc[distribution, 2]=="distribution"
=======
class Reseau(object):
    def __init__(self, list_nodes, distribution):
        assert len(list_nodes)<=30
        assert df_nodes_paris[distribution, 2]=="distribution"
>>>>>>> Karel
        self.list_nodes=list_nodes
        self.distribution= distribution

    def add_chain(self,position, node):
        if len(self.list_nodes)<30:
            self.list_nodes.insert(position, node)
           

    def remove_chain(self, position ):
        if self.list_nodes!=[]:
            self.list_nodes.pop(position)

            
        
    def add_terminal(self, position1, position2, ant):
        n=len(self.list_nodes[position1])
        if n<5:
            self.list_nodes[position1].insert(position2,ant )
            
    def remove_terminal(self,position1, position2):
        n=len(self.list_nodes[position1])
        if n>1:
            self.list_nodes[position1].pop(position2)
    
    def show(self):
        l=[]
        n=len(self.list_nodes)

        for i in range (0, n):
             m=len(self.list_nodes[i])
             for j in range(0,m):
                 l.append ( self.list_nodes[i][j])               
        return l
<<<<<<< HEAD
                 
  
        
m=Reseau([[1,3],[5],[2,6,4]],7)
   
=======
    

def creation_architecture(df_nodes_paris, df_distance_paris):
    l=[False for i in range(len(df_nodes_paris)]
    df_nodes_paris["visited"]=l
    while False in df_nodes_paris["visited"]:
        


        



        
m=Reseau([[1,3],[5],[2,6,4]],7)
>>>>>>> Karel
