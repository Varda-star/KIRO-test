#!/usr/bin/env python
# coding: utf-8

# In[42]:


import json

with open("A.json", "r") as file:
      data = json.load(file)


def get_itin(i,data):
    for k in data["itineraire"]:
        if k["id"]==i:
            return k

def list_trains(data):
    L=[]
    for i in data["trains"]:
        for j in i:
            L.append(j)
    return L
def get_train(i,L):
    for k in L:
        if k["id"]==i:
            return k

def contraintes1(trains,data):
    L=list_trains(data)
    T=True
    for j in trains:
        trainj=get_train(int(j),L)
        solj=trains[j]  
        it=solj["itineraire"]
        itinj=itin(int(it),data)
        if (((it!="notAffected") or (qt!="notAffected")) and ((itinj["voiesAQuai"]!=solj["voiesAQuai"]) or (itinj["voisEnligne"]!=solj["voisEnLigne"]))):
            T=False
    return T


