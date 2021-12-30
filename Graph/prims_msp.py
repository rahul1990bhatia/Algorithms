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


def prims_spanning_tree(graph, source):

    distance_table = {}
    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0,source)

    PriorityQueue = {}
    PriorityQueue[source] = 0

    visited_vertices = set()
    spanning_tree = set()

    while len(PriorityQueue.keys()) > 0:

        min_val = 10000000
        min_key = None
        for key,value in PriorityQueue.items():
            if value < min_val:
                min_val = value
                min_key = key
        PriorityQueue.pop(min_key)
        current_vertex  = min_key
        current_distance = int(distance_table[current_vertex][0])

        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        if current_vertex != source:
            last_vertex = distance_table[current_vertex][1]
            edge = str(last_vertex) + "-->" + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neigbor in graph.get_adjacent_vertices(current_vertex):
            distance = graph.get_edge_weight(current_vertex, neigbor)
            neigbor_distance = distance_table[neigbor][0]

            if neigbor_distance is None or neigbor_distance > distance:
                distance_table[neigbor] = (distance, current_vertex)
                PriorityQueue[neigbor] = distance

    for edge in spanning_tree:
        print(edge)


g = AdjacencyMatrixGraph(8)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)


prims_spanning_tree(g, 1)
print("-------")
prims_spanning_tree(g, 3)
