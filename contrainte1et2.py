#!/usr/bin/env python
# coding: utf-8

# In[14]:


import json

with open("A.json", "r") as file:
      data = json.load(file)


def get_itin(i,data):
    for k in data['itineraires']:
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
        
def in_group(idt,data):
    
    for k in data["trains"]:
        for i in k:
            if i["id"]==idt:
                return k
def get_train_aquai(q,data):
    for k in data["trains"]:
        if k[0]["voieAQuai"]==q:
            return k
def contraintes1(trains,data):
    L=list_trains(data)
    T=True
    for j in trains:
        trainj=get_train(int(j),L)
        solj=trains[j]  
        it=solj['itineraire']
        itinj=get_itin(int(it),data)
        if (((it!="notAffected") or (qt!="notAffected")) and ((itinj["voieAQuai"]!=solj["voieAQuai"]) or (itinj["voisEnligne"]!=solj["voisEnLigne"]))):
            T=False
    return T
def contraintes2(trains,data):
    L=list_trains(data)
    T=True
    for j in trains:
        solj=trains[j]  
        qj=solj["voieAQuai"]
        k=in_group(int(j),data)
        qg=k[0]["voieAQuai"]
        if qj!=qg:
            T=False
    return T

