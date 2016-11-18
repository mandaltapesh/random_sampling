from __future__ import print_function,division
import igraph as ig
from itertools import combinations as c
import pickle as p
import random
#import cogent.maths.stats.test as stats
import scipy.stats
import numpy as np
from math import ceil,fabs




pg = ig.Graph()
g =ig.Graph()

pg=pg.Read_Pickle("karate.pickle")

for v in pg["karate"].vs():
    g.add_vertex(v)

for e in pg["karate"].es():
    g.add_edge(e.source,e.target)
    
#l=g.layout("drl")
#ig.plot(g,layout=l)

n=[]
for v in g.vs():
    n.append(v)


g1=ig.Graph()
g2=ig.Graph()
g3=ig.Graph()
g4=ig.Graph()


g1.add_vertices(3)
g2.add_vertices(3)
g3.add_vertices(3)
g4.add_vertices(3)

g1.add_edges([(0,1),(1,2),(2,0)])
g2.add_edges([(0,1),(1,2)])
g3.add_edges([(0,1)])

def init_d():
    d={}
    d.update({g1:0})
    d.update({g2:0})
    d.update({g3:0})
    d.update({g4:0})
    return d
    
def init_sg():
    sg=[]
    return sg

def rand(s):
    cs=[]
    sample=[]
    for x in c(n,3):
        cs.append(x)
    sample=random.sample(cs,s)
    return sample

def subg(csr):
    sg=init_sg()
    for v in csr:
        sub=g.subgraph(v,"copy_and_delete")
        sg.append(sub)
    return sg
    
def freq_iso(sgr):
    d=init_d()
    for i in d.keys():
        for j in sgr:
            if i.isomorphic(j):
                d[i]=d[i]+1

    #for k in d.keys():
    #    print(k," : ",d[k])

    return d

rs = 5984

acs=rand(rs)
acsg=subg(acs)
dfa=freq_iso(acsg)
fa=dfa.values()
fan=rs
nfa=[fa[0]/fan,fa[1]/fan,fa[2]/fan,fa[3]/fan]


print("--------------------------")

co=0
for nf in range(1,rs):
    fec=[]
    for i in range(0,10):
        ecs=rand(nf)
        ecsg=subg(ecs)
        dfe=freq_iso(ecsg)
        fe=dfe.values()
        fec.append(fe)
    print(nf);
    t1=0
    t2=0
    t3=0
    t4=0

    for v in fec:
        v=list(v)
        t1=t1+v[0]
        t2=t2+v[1]
        t3=t3+v[2]
        t4=t4+v[3]

    fef=[ceil(t1/10),ceil(t2/10),ceil(t3/10),ceil(t4/10)]
    nfef=[fef[0]/nf,fef[1]/nf,fef[2]/nf,fef[3]/nf]

    de=[]
    for i in range(0,4):
        de.append(fabs(nfef[i]-nfa[i]))

    #print("-----------------------------------")
    #print(nfa);
    #print(nfef);
    #print(de);
    #print("-----------------------------------")
    #p=scipy.stats.ks_2samp(nfa,nfef)
    #print(nf,":",p[1])
    
    sde=sum(de)
    
    
    print("sample size=",nf)
    if sde>0.05:
        co+=1
    delta=co/nf
    print("d=",delta);
    if delta<=0.05:
        print("limit reached");
        break
    print("---------------------------");
        
    
    
   
    
    
