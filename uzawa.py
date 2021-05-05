#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:20:00 2021

@author: user
"""

import numpy as np
import math as m
from numpy.linalg import norm

N=10

def GC(a,b,x0,eta,imax):
    x=x0
    g=np.dot(a,x)-b
    d=-g
    g1=np.transpose(g)
    n0=np.dot(g1,g)
    i=0
    resi=[]
    while n0>eta**2 and  i<imax:
        z=np.dot(a,d)
        rho=(-np.vdot(g,d))/(np.vdot(z,d))
       # print (z,rho)
        x=x+rho*d
        g=g+rho*z
        n1=np.vdot(g,g)
        beta=n1/n0
        n0=n1
        d=-g+beta*d
        i=i+1
        resi.append(m.sqrt(n1))
        if m.sqrt(n1)>10**10:
            print("Explosion de GC!!!!!!!")
    if i==imax:
        print("imax a ete atteint dans gc. Augmenter i max")
    return (x,i,resi)


def mat(n):
    b=np.zeros((n,1))
    A=2*np.eye(n)


    for i in range(1,n):
        A[i,i-1]=-1
        A[i-1,i]=-1
        b[i]=i 
   
    return(A,b)
        
(A,b)=mat(N)

x0=b
imax=10000
eta=10**(-3)

on=np.zeros((N,N))
H=np.concatenate((np.concatenate((A, on), axis= 1), np.concatenate((on, A), axis=1) ))

def npmax (lam,mu):
    k=np.zeros((len(lam),1))
    
    for i in range (len(lam)):
        if lam[i][0]>mu[i][0]:
            k[i][0]=lam[i][0]
        else:
            k[i][0]=mu[i][0]
    return k 




def uzawa(H,C,g,f,lam0,rho,eta, eps,imax,N):
    n=0
    z0=np.zeros((2*N,1))
    (u,I,RESI)=GC(H,-(np.dot(np.transpose(C),lam0)+g),z0,eta,imax)
    resi_lam=1
    resi_u=1
    lam=lam0
    while (resi_lam> eta or resi_u>eps) and n<imax:
        z0=u
        lam=npmax(lam+rho*(np.dot(C,u)-f), np.zeros((N,1)))
        (u,i,resi)=GC(H,-(np.dot(np.transpose(C),lam)+g), z0, eta, imax)
        resi_lam=norm(npmax(np.dot(C,u)-f, np.zeros((N,1))))
        resi_u=norm(u-z0)
        n=n+1
    return (u,lam,n,resi_lam,resi_u)

Mtot=40.0
mi=Mtot/(N+2)
g0=9.81       
g=np.zeros((2*N,1))
for i in range (1, N):
    g[N+i][0]=g0*mi
g[0][0]=-2
g[N][0]=-2
g[2*N-1][0]=1
g[N-1][0]=-1
     





C=np.concatenate((np.zeros((N,N)), -np.eye(N)), axis=1)

f=(-1/2)*np.ones((N,1))

lam0=f
rho=0.01
eps=eta
(u,lam,n,resi_lam,resi_u)=uzawa(H,C,g,f,lam0,rho,eta, eps, imax,N)  
        
        
        
        
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        