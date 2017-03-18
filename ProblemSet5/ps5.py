# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#
PATH_TO_MAP = 'C:/Users/Denys/Canopy/studing/edx_MITx_6.00.2x/ProblemSet5/mit_map.txt'
def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    weighted_digraph = WeightedDigraph()
    #print type(weighted_digraph)
    map_data = open(mapFilename, 'r', 0)
    for line in map_data.readlines():
        #print line
        data = line.split()
        #print data
        for node in data[:2]:
            if data.index(node) == 0:
                source = Node(node)
                if source not in weighted_digraph.nodes:
                    weighted_digraph.addNode(source)
            elif data.index(node) == 1:
                destination = Node(node)
                if destination not in weighted_digraph.nodes:
                    weighted_digraph.addNode(destination)
        #print source, destination
        if (source in weighted_digraph.nodes and destination in weighted_digraph.nodes):
            edge = WeightedEdge(source, destination, int(data[2]), int(data[3]))
            print edge
            weighted_digraph.addEdge(edge)
    #print weighted_digraph.edges
    return weighted_digraph

        
#print load_map('C:\Users\Denys\Canopy\studing\edx_MITx_6.00.2x\ProblemSet5\mit_map.txt')
#mitMap = load_map('C:\Users\Denys\Canopy\studing\edx_MITx_6.00.2x\ProblemSet5\mit_map.txt')
#print mitMap
#print mitMap.nodes
#print mitMap.edges
#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def lenOfPath(digraph, path):
    totalDist = 0
    distOutdoors = 0
    #print path[:-1]
    for startNode in range(len(path[:-1])):
        #print path[startNode], path[startNode+1]
        #print "Edge: ", digraph.edges[path[startNode]]
        for destNode in digraph.edges[path[startNode]]:
            #print destNode[0]
            #print destNode[0] == path[startNode+1]
            if destNode[0] == path[startNode+1]:
                totalDist += destNode[1][0]
                distOutdoors += destNode[1][1]
                break
    return totalDist, distOutdoors
    
def DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], seen = [], len_of_path = None, best = None, path_set = [], step = 0):
    #step += 1
    #print 'STEP',step
    #if step > 13:
    #    return 1
    best = best
    len_of_path = len_of_path
    #print path
    path += [start]
    seen += [start]
    #print 'SEEN: ',seen
    if start == end:
        if path not in path_set:
            #print lenOfPath(digraph, path)
            
            if best > lenOfPath(digraph, path) or best == None:
                best = lenOfPath(digraph, path)
                path_set.append(path[:])
                #print 'START = END '*3
                #print 'Path: {0}; Current pos: {1}'.format(path, start)
                #print 'Children of Node({0}): {1}'.format(start, digraph.childrenOf(start))
                #print 'Path set: {0}\n'.format(path_set)
                #print 'LenOfPath: ', len_of_path
                #print 'STEP',step
        return path, path_set, len_of_path, best
        
    #print 'Path: {0}; Current pos: {1}'.format(path, start)
    #print 'Children of Node({0}): {1}'.format(start, digraph.childrenOf(start))
    #print 'Path set: {0}\n'.format(path_set)
    #print 'LenOfPath: ', len_of_path
    for node in digraph.childrenOf(start):
        #print 'Node: ', node
        if node not in path or node == end:
            if maxTotalDist >=  lenOfPath(digraph, path[:]+[node])[0] and maxDistOutdoors >=  lenOfPath(digraph, path[:]+[node])[1]:
                #print 'LenOfPath + Node: ', lenOfPath(digraph, path[:]+[node])
                #print 'Best: ', best
                if best == None or best > lenOfPath(digraph, path[:]+[node]):
                    newPath, path_set, new_len_of_path, best = DFS(digraph, node, end, maxTotalDist, maxDistOutdoors, path, seen, lenOfPath(digraph, path[:]+[node]), best, path_set, step)
                    
                    path.remove(node)  
            #print path   
    #print 'STEP',step
    return path, path_set, len_of_path, best
            
def findShort(digraph, powerSet, maxTotalDist, maxDistOutdoors):
    shortes = None
    for path in powerSet:
        totalDist = 0
        distOutdoors = 0
        #print path[:-1]
        for startNode in range(len(path[:-1])):
            #print path[startNode], path[startNode+1]
            #print "Edge: ", digraph.edges[path[startNode]]
            for destNode in digraph.edges[path[startNode]]:
                #print destNode[0]
                #print destNode[0] == path[startNode+1]
                if destNode[0] == path[startNode+1]:
                    totalDist += destNode[1][0]
                    distOutdoors += destNode[1][1]
                    break
        #print totalDist, distOutdoors
        if totalDist <= maxTotalDist and distOutdoors <= maxDistOutdoors:
            if shortes == None:
                shortes = (path, totalDist, distOutdoors)
            if totalDist < shortes[0]:
                shortes = (path, totalDist, distOutdoors)
        #print 'Shortes: ', shortes
    if shortes == None:
        raise ValueError
        
    return [node.getName() for node in shortes[0]]
        
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #print 'bruteForceSearch'
    #start = Node(start)
    #print start
    #print DFS(digraph, start, Node(end))[1]
    ##print path
    #path, powerSet, len_of_path = None, None, None
    #print path
    powerSet = DFS(digraph, Node(start), Node(end), maxTotalDist, maxDistOutdoors, path = [], seen = [], len_of_path = None, best = None, path_set = [], step = 0)[1]
    #print powerSet, digraph.edges[Node('1')]
    #print powerSet
    shortes = findShort(digraph, powerSet, maxTotalDist, maxDistOutdoors)
    return shortes

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

#Uncomment below when ready to test
## NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #Test cases
    mitMap = load_map(PATH_TO_MAP)
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes, len(mitMap.nodes)
    print 'edges', mitMap.edges
    

    LARGE_DIST = 1000000
#
#   Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    #DFS = DFS(mitMap, Node('32'), Node('56'))
    #print DFS
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        print bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
