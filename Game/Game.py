import numpy as np
from Automata import dfa 


ni=6
nj=9
S=np.ones((ni,nj))
rotlist=np.array([1,2,3,4])


#inserting S
for i in range(ni):
    for j in range(nj):
        if i==0  or j in range(3) or i==ni-1 or j==nj-1:
            S[i,j]=0


for j in range(3):
    S[1,j]=1

print(S)

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





Sp=np.copy(S)
d=2
xh=np.array([1,2,1])
Ins=''
while True:
    Sp=np.copy(S)
    robo=input("Enter robot actoin f or r")
    df=dirflag(xh,d)
    rf=rotflag(xh,S)
    Ins=Ins+(trIn(rf,df))
    ac=(action(xh[0],xh[1],S))
    DfaOut=dfa.read_input(Ins)
    if DfaOut=='S1':
        if  ac[xh[2]-1]==1:
            if robo=='f':
                xh=move(xh,1)
                rf=rotflag(xh,S)
                df=dirflag(xh,d)
    elif DfaOut=='S2':
        if robo=='r':
            print('Rotated')
            xh[2]=rotlist[xh[2]]
            rf=rotflag(xh,S)
            df=dirflag(xh,d)
    elif DfaOut=='S3':
        print('Finished ###')
        if robo=='r':
            print('Rotated')
            xh[2]=rotlist[xh[2]]
            rf=rotflag(xh,S)
            df=dirflag(xh,d)
        #break
    Sp[xh[0],xh[1]]=3
    xr=move(xh,-2)
    Sp[xr[0],xr[1]]=2
    print(Sp)
    print(df,rf,DfaOut,robo,xh)
