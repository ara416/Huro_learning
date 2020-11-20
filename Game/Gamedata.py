import numpy as np
from Automata import dfa 


ni=10
nj=12
S=np.ones((ni,nj))
rotlist=np.array([1,2,3,4])


#inserting S
for i in range(ni):
    for j in range(nj):
        if i==0  or j in range(3) or i in range(ni-2,ni) or j in range(nj-2,nj):
            S[i,j]=0


for j in range(3):
    S[1,j]=1


# extension map each x = i,j,k where i and j are the position on the map and 
# k is the direction of the bar. Since Bar is know and every thing :p
# set direction as r u l d


def rotflag(x,S):
    if x[2]==1:
       rf=(np.sum(S[x[0]+range(3),:][:,x[1]-range(3)]))==9
    elif x[2]==2:
       rf=(np.sum(S[x[0]+range(3),:][:,x[1]+range(3)]))==9
    elif x[2]==3:
       rf=(np.sum(S[x[0]-range(3),:][:,x[1]+range(3)]))==9
    elif x[2]==4:
       rf=(np.sum(S[x[0]-range(3),:][:,x[1]-range(3)]))==9
    return(rf)

def move(x,d):
    xd=np.copy(x)
    if xd[2]==1:
        xd[1]=xd[1]+d
    elif xd[2]==2:
        xd[0]=xd[0]-d
    elif xd[2]==3:
        xd[1]=xd[1]-d
    elif xd[2]==4:
        xd[0]=xd[0]+d
    return(xd)


def move2(x,a):
    xd=np.copy(x)
    if a==0:
        xd[1]=xd[1]+1
    elif a==1:
        xd[0]=xd[0]-1
    elif a==2:
        xd[1]=xd[1]-1
    elif a==3:
        xd[0]=xd[0]+1
    return(xd)


def moveprob(x,a,S):
    pf=np.array([0,0,0,0])
    if x[2]==1:
        for j in range(4):
            xr=move2(x,j)
            pf[j]=(np.sum(S[xr[0]+range(3),:][:,xr[1]-range(3)]))
    elif x[2]==2:
        for j in range(4):
            xr=move2(x,j)
            pf[j]=(np.sum(S[xr[0]+range(3),:][:,xr[1]+range(3)]))
    elif x[2]==3:
        for j in range(4):
            xr=move2(x,j)
            pf[j]=(np.sum(S[xr[0]-range(3),:][:,xr[1]+range(3)]))
    elif x[2]==4:
        for j in range(4):
            xr=move2(x,j)
            pf[j]=(np.sum(S[xr[0]-range(3),:][:,xr[1]-range(3)]))
    return(np.multiply(pf,a))

def dirflag(x,d):
    return(x[2]==d)




def action(i,j,S):
    a=np.array([S[i,j+1],S[i-1,j],S[i,j-1],S[i+1,j]])# possible actions r u l d
    return(a)


def trIn(rf,df):
    if df:
        return '1'
    else:
        if rf:
            return '2'
        else:
            return '3'


