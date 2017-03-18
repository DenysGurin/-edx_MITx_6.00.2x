import itertools 
pset = itertools.product('ABC', repeat = 2)
n = 0
items = 'ABC'
print items[0]

for i in itertools.product(xrange(3), repeat =3):
    #n+=1
    items = 'ABC'
    bag1 = []
    bag2 = []
    item = 0
    #print i
    for j in i:
        #print j, item, items[item]
        
        if int(j) == 1:
            #print 'bag1.append(items[item])'
            bag1.append(items[item])
        elif int(j) == 2:
            bag2.append(items[item])
        item += 1
    print (bag1,bag2)#, n
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            if (i / (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i / (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
for i in powerSet('ABC'):
    print i
for n in yieldAllCombos('ABC'):
    print n