def powerSet(listOf):
    #print listOf
    if len(listOf) == 0:
        return [[]]
    else:
        cutList = powerSet(listOf[1:])
        firstElem = [listOf[0]]
        withFirst = []
        for cut in cutList:
            #print cut+firstElem
            withFirst.append(cut + firstElem)
    allOf = cutList + withFirst
    return allOf 
    
print powerSet([1, 2, 3, 4, 5])