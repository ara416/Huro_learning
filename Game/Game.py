import numpy as np
import matplotlib.pyplot as plt
from Automata import dfa
from Gamedata import *
d=2
xh=np.array([1,2,1])


Sp=np.copy(S)
Sp[xh[0],xh[1]]=3
xr=move(xh,-2)
Sp[xr[0],xr[1]]=2
print('=========================Initail ===========================')
print(Sp)
Ins=''
ac=action(xh[0],xh[1],S)
print(np.argmax(moveprob(xh,ac,S)))
while True:
    Sp=np.copy(S)
    while True:
        robo=input("Enter robot actoin f or r: \t")
        if robo=='r'or robo=='f':
            break
        else:
            print('Please input f or r')
    df=dirflag(xh,d)
    rf=rotflag(xh,S)
    Ins=Ins+(trIn(rf,df))
    ac=(action(xh[0],xh[1],S))
    DfaOut=dfa.read_input(Ins)
    if DfaOut=='S1':
#        if  ac[xh[2]-1]==1:
        if robo=='f':
           # xh=move(xh,1)
            xh=move2(xh,np.argmax(moveprob(xh,ac,S)))
            print("mover direction",moveprob(xh,ac,S))
            rf=rotflag(xh,S)
            df=dirflag(xh,d)
    elif DfaOut=='S2':# make this a function that takes S and robo and xh , df
        if robo=='r':
            print('Waiting for rotation')
            xh[2]=rotlist[np.remainder(xh[2],4)]
            rf=rotflag(xh,S)
            df=dirflag(xh,d)
        else:
           print('Rotate or Wait')
    elif DfaOut=='S3':
        print('Direction is corrected')
        if robo=='r':
            print('Rotated')
            if rf==True:
                xh[2]=rotlist[np.remainder(xh[2],4)]
            else:
                print('Rotation is not possible')
            rf=rotflag(xh,S)
            df=dirflag(xh,d)
        #break
    Sp[xh[0],xh[1]]=3
    xr=move(xh,-2)
    Sp[xr[0],xr[1]]=2
    Ins=Ins+(trIn(rf,df))
    DfaOut=dfa.read_input(Ins)
    print(Sp)
    print('DF','RF','DFA','Input','xh',sep='\t')
    print(df,rf,DfaOut,robo,xh,sep='\t')
    print('====================================================')
