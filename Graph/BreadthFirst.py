from queue import Queue
import numpy as np

import abc          #abstract base class
import numpy as np


#####Adjacency Matrix#########
# You should use adjacency matrix for small densily connected graphs
# space complexity O(V^2)

############################################################
#Base Class representation of class with all interface methods
############################################################

class graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass



#################################################################
# Represent the graph as adjacency matrix
#################################################################

class AdjacencyMatrixGraph(graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph,self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices,numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" %(v1, v2))

        if weight < 1:
            raise ValueError("An edge weight cannot be < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Can't access vertex %d" % v)

        adjacent_vertices = []

        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Can't access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" %(v1, v2))

        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


def breadth_first(graph ,start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex =  queue.get()
        if visited[vertex] == 1:
            continue

        print("Visit : ", vertex)
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)

def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return
    visited[current] = 1
    print("Visit : ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph,visited,vertex)


print("-------->BFS<------------")
g  = AdjacencyMatrixGraph(9)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)
breadth_first(g,2)

print("Directed")
g  = AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)
breadth_first(g,0)

print("-------->DFS<------------")
g  = AdjacencyMatrixGraph(9)
visited = np.zeros(g.numVertices)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)
depth_first(g,visited,2)

print("Directed")
g  = AdjacencyMatrixGraph(9, directed=True)
visited = np.zeros(g.numVertices)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,7)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(1,5)
g.add_edge(5,6)
g.add_edge(6,3)
g.add_edge(3,4)
g.add_edge(6,8)
depth_first(g,visited,0)

