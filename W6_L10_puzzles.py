class Puzzle(object):
    """
    """
    def __init__(self, order):
        self.lable = order
        self.spot = None
        for index in range(9): # [0,1,2,3,4,5,6,7,8]
            #print order[index] == '0'
            if order[index] == '0':
                self.spot = index
                break
                
    def transition(self, to):
        lable = self.lable
        blankLocation = self.spot
        newBlankLocation = str(lable[to])
        newLable = ''
        #print self.spot
        for index in range(9):
            #print newBlankLocation
            if index == to:
                newLable += '0'
            elif index == blankLocation:
                newLable += newBlankLocation
            else:
                newLable += str(lable[index])
        return Puzzle(newLable)
        
    def __str__(self):
        return self.lable
    def __repr__(self):
        return self.lable
    def __eq__(self, other):
        return self.lable == other.lable
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return hash(self.lable)

def shiftDict():
    shiftDict = {}
    shiftDict[0] = [1, 3]
    shiftDict[1] = [0, 2, 4]
    shiftDict[2] = [1, 5]
    shiftDict[3] = [0, 4, 6]
    shiftDict[4] = [1, 3, 5, 7]
    shiftDict[5] = [2, 4, 8]
    shiftDict[6] = [3, 7]
    shiftDict[7] = [4, 6, 8]
    shiftDict[8] = [5, 7]
    return shiftDict

def interactivePuzzle(init, goal):
    print init.spot
    while init != goal:
        print "Puzzl: "
        for s in [0,3,6]:
            print init.lable[s:s+3]
        to = raw_input("Enter 'to': ")
        init = init.transition(int(to))
    print "Finish:\n",init
    
def DFSshortes(start, end, path = [], best = None, shiftDict = shiftDict(), step = 0):
    if step > 1000:
        return 1
    step += 1
    path.append(start)
    print len(path)
    #print path, shiftDict[start.spot]
    #print start == end
    #print "Best: {0}".format(best)
    if start == end:
        best = path[:]
        #print "Best: {0}".format(best)
        return best, path
    for child in shiftDict[start.spot]:
        new = start.transition(child)
        #print new, path, best
        if new not in path:
            if best == None or len(best) > len(path):
                best, path = DFSshortes(new, end, path, best, shiftDict, step)  
    #print best
    return best
    
def BFS(start, end, queue = [], shift = shiftDict()):
    
    #path = [start]
    queue.append([start])
    #queue.extend(shift[start.spot])
    #print "Queue: {0}".format(queue)
    while len(queue) > 0:
        temporaryPath = queue[0]
        lastInPath = temporaryPath[-1]
        #print "Queue: {0}\n".format(queue)
        #print "Temporary Path: {1}".format(queue, temporaryPath)
        for pos in shift[lastInPath.spot]:
            puzzle = lastInPath.transition(pos)
            if puzzle not in temporaryPath:            
                queue.append(temporaryPath + [puzzle])
                #print "Queue: {0}\n".format(queue)
                #print "Temporary Path: {1}\nPuzzle: {2}".format(queue, temporaryPath, puzzle)
                #print "Puzzle: {0}".format(puzzle)
                if puzzle == end:
                    return temporaryPath + [puzzle]
        del queue[0]
    return None
    
def printPuzzle(puzzle):  
    for cell in range(7):
        if cell%3 == 0:
            print "{0}".format(puzzle.lable[cell:cell+3])
        

    
def printSolution(solution):
    num = 0
    for step in solution:
        num += 1
        print "\nStep number {0}:\n".format(num)
        printPuzzle(step)
    
#printPuzzle(Puzzle("123456780"))
#printSolution([Puzzle("123045678"), Puzzle("012345678")])
#print DFSshortes(Puzzle("123045678"), Puzzle("012345678"))
#a = Puzzle("123456780")
#print a
solution = BFS(Puzzle("134265870"), Puzzle("123456780"))
printSolution(solution)