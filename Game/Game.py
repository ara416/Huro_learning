import numpy as np


ni=6
nj=6
Sp=np.ones((ni,nj))
objdir=np.array([0,1])#[+-1 +-1]

# Sp[1,0]=-1 # in door
# Sp[0,2]=2 # out door

for i in range(ni):
    for j in range(nj):
        if i==0 or j==0 or i==ni-1 or j==nj-1:
            Sp[i,j]=0

def action(i,j,S):
    a=np.array([S[i+1,j],S[i-1,j],S[i,j+1],S[i,j-1]])# possible actions v^><
    return(a)

def rotflg(xr,xh,Sp):
    d=xr-xh;
    z=np.array([0,0,1])
    r=np.delete(np.cross(np.append(d,0),z),-1)
    flg=np.array([Sp[tuple(xr-r)],Sp[tuple(xr+r)]])
    return flg

def bardir(xh,xr):
    return(xh-xr)/np.linalg.norm(xh-xr)


xh=np.array([1,2])
xr=np.array([1,0])

# def rotfg(xh,xr):
#     rf=np.zeros((1,4))
#     if


# def dirtoaction(x):



# def rotavl(bo,fo,):

# print(r)
print(Sp)
