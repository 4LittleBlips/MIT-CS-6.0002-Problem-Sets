
class Node(object):
    '''
    Node Object has name attribute
    '''
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.getName()


class Edge(object):
    '''
    Edge object used to link two nodes in one direction.
    Links src attribute to dest attribute
    '''
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def __str__(self):
        edge = "{0} -> {1}".format(self.getSrc(), self.getDest())
        return edge


class Digraph(object):
    '''
    Nodes are stored as keys in dictionary
    Linked nodes are values in list associated with keys
    '''

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        self.edges[node] = []

    def makeEdge(self, edge):
        try:
            assert edge.getSrc() in self.edges, 'Source Node does not exist.'
            assert edge.getDest() in self.edges, 'Destination Node does not exist.'
            assert edge.getDest() not in self.edges[edge.getSrc()], 'Edge already exists'

        except AssertionError:
            return self.edges
        

        self.edges[edge.getSrc()].append(edge.getDest())
        return self.edges
    
    def getNeighbors(self, node):
        return self.edges[node]

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += "{0} -> {1}".format(src, dest) + '\n'

        return result[:-1]

def printPath(path):
    result = ''
    for node in path:
        result += node.getName() + '->'
    print(result[:-2])

def getAncestry(node, parents):
    if parents[node] == None:
        return [node]
    else:
        ancestry = getAncestry(parents[node], parents)
        return ancestry + [node] 


class Graph(Digraph):
    def makeEdge(self, edge):
        Digraph.makeEdge(self, edge)
        reverse = Edge(edge.getDest(), edge.getSrc())
        Digraph.makeEdge(self, reverse)
        return self.edges


#Nodes

s = Node('S')
a = Node('A')
z = Node('Z')
b = Node('B')
c = Node('C')
d = Node('D')

nodes = [s, z, a, b, c, d]

#Edges
e1 = Edge(s, a)
e2 = Edge(a, z)
e3 = Edge(s, b)
e4 = Edge(b, c)
e5 = Edge(b ,d)
e6 = Edge(c, d)

edges = [e1, e2, e3, e4, e5, e6]

#Graph

g = Graph()

for node in nodes:
    g.addNode(node)

for edge in edges:
    g.makeEdge(edge)
print(g)

def BFS_1(graph, start, end):
    levels = {start: 0}
    parents = {start: None}
    i = 1
    frontier = [start]
    while frontier != []:
        next_frontier = []
        for node in frontier:

            for child in graph.getNeighbors(node):

                if not child in levels:
                    print("Visiting {}".format(child))
                    levels[child] = i
                    parents[child] = node
                    next_frontier.append(child)
                

                else:
                    print("Already visited {}".format(child))

                if child.getName() == end.getName():
                    path = getAncestry(child, parents)
                    return path
        i += 1
        frontier = next_frontier

print("Breadth-First Search S -> Z(Ancestry Implementation): \n")
printPath(BFS_1(g, s, z))



def BFS_2(graph, start, end):
    pathQueue = [[start]]
    
    while pathQueue:
        lastPath = pathQueue.pop(0) #returns and removes first path in Queue
        lastNode = lastPath[-1]     #last node in the path
        print(f"Visiting {lastNode}")
        if lastNode == end:
            return lastPath

        for child in graph.getNeighbors(lastNode):
            if not child in lastPath:
                newPath = lastPath + [child]
                pathQueue.append(newPath)

            else:
                print(f"Already Visited {child}")

    return None

print("Breadth-First Search S -> C (Qeueue Implementation): \n")
printPath(BFS_2(g, s, c))



#Depth First Search


def DFS(graph, start, end, path=[], shortest=None):
    path = path + [start]
    
    if start == end:
        return path
    
    print("Current Path: ", end="")
    printPath(path)
    
    for child in graph.getNeighbors(start):
        
        if child not in path:
            
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, child, end, path, shortest)        
                
                if newPath != None:
                    shortest = newPath
                elif newPath == None and shortest != None:
                    shortest = shortest[:-1]    # Removes last node in path if that node leads to an impass
    
    return shortest

print("Depth-First Search (S -> D): \n")
printPath(DFS(g, s, d))

print("Depth-First Search (Z -> B): \n")
printPath(DFS(g, z, b))















