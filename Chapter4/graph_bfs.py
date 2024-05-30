
# Listing L4.5; File: graph_bfs.py
# Plus extra output features

from typing import TypeVar, Generic, List, Optional
from edge import Edge

import sys
sys.path.insert(0,'..')
from Chapter2.generic_search import bfs, Node, node_to_path

V = TypeVar('V') # type of the vertices in the graph

# CityGraph data structure is a List, when each entry is a list of Edges
#  C[0] = [
#          [ Edge,   # (u:0, v: 5)  Seattle -> Chicago
#            Edge]   # (u:0, v: 1)  Seattle -> San Francisco
#         ]


class Graph(Generic[V]):
    #--------------------------------------------------------------
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] =  [ [] for _ in vertices]
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
        self.add_edge(edge)
    #--------------------------------------------------------------
    # Add an edge by looking up vertex indices (convenince method)
    def add_edge_by_vertices(self, first: V, second : V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u,v)
    #--------------------------------------------------------------
    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]
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
           #print("@@ self.vertex_at[{a}] returned: <{b}>".format(a=i,b=self.vertex_at(i)) )
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc
    #--------------------------------------------------------------

if __name__ == "__main__":

   # Find callable methods of Graph
   graph_methods = [method_name for method_name in dir(Graph)
                     if callable(getattr(Graph, method_name))]
  #print("@@ Graph_methods: <{a}>".format(a=graph_methods) )

   # Find callable methods of Edge
   edge_methods = [method_name for method_name in dir(Edge)
                     if callable(getattr(Edge, method_name))]
  #print("@@ Edge_methods: <{a}>".format(a=edge_methods) )

   # test basic Graph construction
   city_graph:Graph[str] = Graph(
    [
     "Seattle","San Francisco", "Los Angeles", "Riverside", "Phoenix","Chicago",
     "Boston","New York", "Atlanta","Miami", "Dallas","Houston", "Detroit","Philadelphia",
     "Washington"
    ]
   )

   city_graph.add_edge_by_vertices("Seattle","Chicago")
   city_graph.add_edge_by_vertices("Seattle","San Francisco")

   city_graph.add_edge_by_vertices("San Francisco","Riverside")
   city_graph.add_edge_by_vertices("San Francisco","Los Angeles")

   city_graph.add_edge_by_vertices("Los Angeles","Riverside")
   city_graph.add_edge_by_vertices("Los Angeles","Phoenix")

   city_graph.add_edge_by_vertices("Riverside","Phoenix")
   city_graph.add_edge_by_vertices("Riverside","Chicago")

   city_graph.add_edge_by_vertices("Phoenix","Dallas")
   city_graph.add_edge_by_vertices("Phoenix","Houston")

   city_graph.add_edge_by_vertices("Dallas","Chicago")
   city_graph.add_edge_by_vertices("Dallas","Atlanta")
   city_graph.add_edge_by_vertices("Dallas","Houston")

   city_graph.add_edge_by_vertices("Houston","Atlanta")
   city_graph.add_edge_by_vertices("Houston","Miami")

   city_graph.add_edge_by_vertices("Atlanta","Chicago")
   city_graph.add_edge_by_vertices("Atlanta","Washington")
   city_graph.add_edge_by_vertices("Atlanta","Miami")

   city_graph.add_edge_by_vertices("Miami","Washington")

   city_graph.add_edge_by_vertices("Chicago","Detroit")

   city_graph.add_edge_by_vertices("Detroit","Boston")
   city_graph.add_edge_by_vertices("Detroit","Washington")
   city_graph.add_edge_by_vertices("Detroit","New York")

   city_graph.add_edge_by_vertices("Boston","New York")

   city_graph.add_edge_by_vertices("New York","Philadelphia")

   city_graph.add_edge_by_vertices("Philadelphia","Washington")

   print(city_graph) # Depends of __str__ defined here

   print("=============")
   for i in range(0,len(city_graph._edges)):
      print("City[{a:02d}]: <{b}>".format(
		a=i,b=city_graph.vertex_at(i)) )
      A = city_graph.vertex_at(i)
      B = city_graph._edges[i]
      C = len(city_graph._edges[i])
      for i2 in range(0,C):
         E_u = city_graph._edges[i][i2].u
         E_u_name = city_graph.vertex_at(E_u)
         E_v = city_graph._edges[i][i2].v
         E_v_name = city_graph.vertex_at(E_v)
         print("\t ({a}) {b} => {d} ({c})".format(a=E_u,b=E_u_name,c=E_v,d=E_v_name) )
      print("=============")

#%%S
   print(" ")
   # The ':Optional [Node[V]]' is not required. I think it was added to clarify
   # what 'bfs' is passing back.
   bfs_result: Optional [Node[V]] = bfs("Boston",
                                        lambda x: x == 'Miami',
                                        city_graph.neighbors_for_vertex)
   if bfs_result is None:
      print("No solution found using breadth-first search")
   else:
      # 'List[V]' is a cast of result to 'path'
      path: List[V] = node_to_path(bfs_result)
      print("Path from Boston to Miami")
      print(path)
#%%E

# -- end of file
