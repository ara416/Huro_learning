import mtl
phi0 = mtl.parse('atomicpred')

data = {
    'a': [(0, True)],
    'b': [(0, True)]
}
#phi = mtl.parse ('(F ~a) ->b' )
phi = mtl.parse('(a -> b -> c)')
print(phi)

data['a'].append((1,False))
#print(data)
#print(phi(data))
