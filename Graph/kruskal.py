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



def spanning_tree(graph):
    priority_queue = {}

    for v in range(graph.numVertices):
        for neigbor in graph.get_adjacent_vertices(v):
            priority_queue[(v,neigbor)] = graph.get_edge_weight(v, neigbor)

    visited_vertices = set()
    spanning_tree_dict = {}

    for v in range(graph.numVertices):
        spanning_tree_dict[v] = set()


    num_edge = 0

    while  len(priority_queue.keys()) > 0 and num_edge < graph.numVertices - 1:
        min_val = 10000000
        min_key = None
        for key,value in priority_queue.items():
            if value < min_val:
                min_val = value
                min_key = key
        priority_queue.pop(min_key)
        v1, v2 = min_key

        if v1  in spanning_tree_dict[v2]:
            continue

        vertex_pair = sorted([v1,v2])

        spanning_tree_dict[vertex_pair[0]].add(vertex_pair[1])

        if has_cycle(spanning_tree_dict):
            spanning_tree_dict[vertex_pair[0]].remove(vertex_pair[1])
            continue

        num_edge = num_edge + 1
        visited_vertices.add(v1)
        visited_vertices.add(v2)

    print("visited_vertices: ", visited_vertices)

    if len(visited_vertices) != graph.numVertices:
        print("Minimum spanning tree not found!")
    else:
        print("Spanning tree found")
        for key in spanning_tree_dict:
            for value in spanning_tree_dict[key]:
                print(key, "-->", value)

def has_cycle(spanning_tree):

    for source in spanning_tree:
        q = []
        q.append(source)

        visited_vertices = set()
        while len(q) > 0:
            vertex = q.pop(0)

            if vertex in visited_vertices:
                return True

            visited_vertices.add(vertex)
            q.extend(spanning_tree[vertex])

    return False

g = AdjacencyMatrixGraph(8)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 2)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)


spanning_tree(g)
