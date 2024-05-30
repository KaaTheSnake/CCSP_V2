# File: graph_FAIL.py
# -- Do not accidently include a level_1 func
# -- 'vertex_count' inside of another level_1
# -- func '__init__'. See line 22 for example.

from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V') # type of the vertices in the graph

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        print("vertices: {a}, _vertices: {b}".format(
          a=vertices,b=self._vertices) )
        self._edges: List[List[Edge]] =  [ [] for _ in vertices]
        for i in self._vertices:
          print("i: {a}".format(a=i) )
        print("_edges: {a}".format(a=self._edges) )
        #--------------------------------------------------------------
        @property
        def vertex_count(self) -> int:
            return len(self._vertices) # Number of vertices
        #--------------------------------------------------------------
        @property
        def edge_count(self) -> int:
            return sum(map(len, self._edges)) # Number of edges
        #--------------------------------------------------------------
        # Add a vertex to the graph and return its index
        def add_vertex(self, vertex: V) -> int:
            self._vertices.append(vertex)
            self._edges.append([]) # Add empty list for containing edges
        return self.vertex_count - 1 # Return index of added vertex
        #--------------------------------------------------------------
        # This is an undirected graph
        # so we always add edges in both directions
        def add_edge(self, edge: Edge) -> None:
            self._edges[edge.u].append(edge)
            self._edges[edge.v].append(edge.reversed())
        #--------------------------------------------------------------
        # Add an edge using vertex indices (convenience method)
        def add_edge_by_indices(self, u: int, v: int) -> None:
            edge: Edge = Edge(u,v)
            self.add_ede(edge)
        #--------------------------------------------------------------
        # Add an edge by looking up vertex vertex indices (convenince method)
        def add_edge_by_vertices(self, first: V, second : V) -> None:
            u: int = self._vertices.index(first)
            print("@@ first: {a}, u: {b}".format(a=first,b=u) )
            v: int = self._vertices.index(second)
            print("@@ second: {a}, v: {b}".format(a=second,b=v) )
            self.add_edge_by_indices(u,v)
        #--------------------------------------------------------------
        # Find the vertex at a specific index
        def vertex_at(self, index: int) -> V:
            return self._vertices(index)
        #--------------------------------------------------------------
        # Find the index of a vertex in the graph
        def index_of(self, vertex: V) -> int:
            return self._vertices.index(vertex)
        #--------------------------------------------------------------
        # Find the vertices that a vertex at some index is connected to
        def neighbors_for_index(self, index: int) -> List[V]:
            return list(map(self.vertex_at, [e.v for e in self._edges[index]]))
        #--------------------------------------------------------------
        # Look up a vertice's index and its neighbors (convenience method)
        def neighbors_for_vertex(self, vertex: V) -> List[V]:
            return self.neighbors_for_index(self.index_of(vertex))
        #--------------------------------------------------------------
        # Return all of the edges associated with a vertex at some index
        def edges_for_index(self, index: int) -> List[Edge]:
            return self._edges[index]
        #--------------------------------------------------------------
        # Look up the index of a vertex and return its edges (convencience method)
        def edges_for_vertex(self, vertex: V) -> List[V]:
            return self.edges_for_index(self.index_of(vertex))
        #--------------------------------------------------------------
        # Make it easy to pretty print a Graph
        def __str__(self) -> str:
            desc: str = ""
            for i in range(self.vertex_count):
                desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
            return desc
        #--------------------------------------------------------------

# -- end of file

if __name__ == "__main__":
   # test basic Graph construction
   city_graph:Graph[str] = Graph([
     "Seattle","San Francisco",
     "Los Angeles", "Riverside",
     "Phoenix","Chicago",
     "Boston","New York",
     "Atlanta","Miami",
     "Dallas","Houston",
     "Detroit","Philadelphia",
     "Washington"]
   )
   A = 1
   print("dir(city_graph):\n <{a}>\n".format(a=dir(city_graph)) )
#  city_graph.add_edge_by_vertices("Seattle","Chicago")
