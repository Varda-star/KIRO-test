import pandas as pd 
import os
df_nodes_nice=pd.read_csv(os.path.join("nice","nodes.csv"), sep=";")
df_nodes_paris=pd.read_csv(os.path.join("paris","nodes.csv"), sep=";")
df_nodes_grenoble=pd.read_csv(os.path.join("grenoble","nodes.csv"), sep=";")
df_distance_nice=pd.read_csv(os.path.join("nice","distances.csv"), sep=";")
df_distance_paris=pd.read_csv(os.path.join("paris","distances.csv"), sep=";")
df_distance_grenoble=pd.read_csv(os.path.join("grenoble","distances.csv"), sep=";")
def ville():
    