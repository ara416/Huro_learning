from ltlf2dfa.parser.ltlf import LTLfParser

parser = LTLfParser()
formula_str ="a"; 
formula = parser(formula_str)       # returns an LTLfFormula

print(formula)                      # prints "G(a -> X (b))"
dfa = formula.to_dfa()
print(dfa)
#print(type(dfa))
