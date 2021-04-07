# Class for node
class node:
    __slots__ = ('movie','neighbor')

# Node constructor
def mkNode(name):
    n = node
    n.name = name
    return

# Find if node is in the graph
def findNode(nodelist, name):
    for n in nodelist:
        if n == None:
            return None
        elif n.name == name:
            return

#Creates graph
def loadGraphFile(file):
    graph = []
    for line in file:
        contents = line.split()
        movieName = contents[0]
        actorName = contents[1:]
        movieNode = findNode(graph, movieName)
        if movieNode == None:
            movieNode = mkNode(movieName)
            graph.append(movieNode)
        actorNode = findNode(graph,actorName)
        if actorNode == None:
            actorNode = mkNode(actorName)
            graph.append(actorNode)
        actorNode.neighbor.append(movieNode)
        movieNode.neighbor.append(actorNode)
    return graph

# Searches graph for path
def search(start,goal,visited):
    if start == goal:
        return [start]
    else:
        for n in start.neighbor:
            content = line.split()
            for x in range(0,(len(content)-1),2):
                z = (content[x] + content[x+1])
                if not z in visited:
                    visited.append(z)
                    path = search(z,goal,visited)
                    if path != None:
                        return [start] + path
                    visited.append(x)