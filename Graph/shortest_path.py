from queue import Queue


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

def build_distance_table(graph, source):

    distance_table  = {}
    for i in range(graph.numVertices):
        distance_table[i] = (None,None)

    distance_table[source] = (0,source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        current_distance = distance_table[current_vertex][0]

        for neighbors in graph.get_adjacent_vertices(current_vertex):
            if distance_table[neighbors][0] is None:
                distance_table[neighbors] = (1+current_distance,current_vertex)

                if len(graph.get_adjacent_vertices(neighbors)) > 0:
                    queue.put(neighbors)

    return distance_table

def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)

    path = [destination] #stack
    previous_vertex  = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print("There is no path from %d to %d" % (source, destination))
    else:
        path = [source] + path
        print("Shortest path is : ", path)

g = AdjacencyMatrixGraph(8)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(3,6)
g.add_edge(6,7)
g.add_edge(0,7)

shortest_path(g,0, 5)
shortest_path(g,0, 6)
shortest_path(g,7, 4)

print("directed graph")
g = AdjacencyMatrixGraph(8, True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(5,4)
g.add_edge(3,6)
g.add_edge(6,7)
g.add_edge(0,7)

shortest_path(g,0, 5)
shortest_path(g,0, 6)
shortest_path(g,7, 4)
