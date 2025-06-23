"""
Basic graph implementation
"""

from .matrix import Matrix


class Graph:
    def __init__(self, vertices, name=None):
        self._vertices = vertices.copy()
        self._edges = Matrix.identity(vertices)
        self._name = name


    def set_arc(self, u, v, weight=1):
        self._edges[u,v] = weight


    def add_edge(self, u, v):
        self.set_arc(u, v)
        self.set_arc(v, u)

    
    def del_edge(self, u, v):
        self.set_arc(u, v, 0)
        self.set_arc(v, u, 0)

    
    def __str__(self):
        return str(self._edges)


    def connected_components():
        """
        Returns a list of lists 
        """
        pass