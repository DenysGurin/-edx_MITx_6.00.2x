def mean(claster):
    return float(sum(claster))/len(claster)

def variance(claster):
    m = mean(claster)
    return sum([(m - element)**2 for element in claster])

def variance1(claster):
    m = mean(claster)
    return sum([(m - element)**2 for element in claster])/len(claster)
    
def badness(clasterSet):
    return sum([variance(claster) for claster in clasterSet])
    
def badness1(clasterSet):
    return sum([variance1(claster) for claster in clasterSet])
    
C1 = [2, 2, -6, -6]
C2 = [-4, -4, 2]

print variance(C1)
print variance(C2)
print badness([C1, C2])

print variance([2, 2, 2])
print variance([-6, -6, -4, -4])
print badness([[2, 2, 2], [-6, -6, -4, -4]])

print variance1(C1)
print variance1(C2)
print badness1([C1, C2])