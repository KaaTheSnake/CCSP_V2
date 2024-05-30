# weighted_graph.py
# From Classic Computer Science Problems in Python Chapter 4
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Listing 4.(7-8); File: weighted_graph.py

from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V') # type of the vertices in the graph

class WeightedGraph(Generic[V], Graph[V]):
    #--------------------------------------------------------------
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] =  [[] for _ in vertices] 

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge) # call superclass version

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
       #    q = self.vertex_at(i)
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc
       #return q

if __name__ == "__main__":
   # test basic Graph construction
   city_graph2: WeightedGraph[str] = WeightedGraph(
    [
     "Seattle","San Francisco", "Los Angeles", "Riverside", "Phoenix","Chicago",
     "Boston","New York", "Atlanta","Miami", "Dallas","Houston", "Detroit","Philadelphia",
     "Washington"
    ]
   )

   city_graph2.add_edge_by_vertices("Seattle","Chicago",1737)
   city_graph2.add_edge_by_vertices("Seattle","San Francisco",678)

   city_graph2.add_edge_by_vertices("San Francisco","Riverside",386)
   city_graph2.add_edge_by_vertices("San Francisco","Los Angeles",348)

   city_graph2.add_edge_by_vertices("Los Angeles","Riverside",50)
   city_graph2.add_edge_by_vertices("Los Angeles","Phoenix",357)

   city_graph2.add_edge_by_vertices("Riverside","Phoenix",307)
   city_graph2.add_edge_by_vertices("Riverside","Chicago",1704)

   city_graph2.add_edge_by_vertices("Phoenix","Dallas",887)
   city_graph2.add_edge_by_vertices("Phoenix","Houston",1015)

   city_graph2.add_edge_by_vertices("Dallas","Chicago",805)
   city_graph2.add_edge_by_vertices("Dallas","Atlanta",721)
   city_graph2.add_edge_by_vertices("Dallas","Houston",225)

   city_graph2.add_edge_by_vertices("Houston","Atlanta",702)
   city_graph2.add_edge_by_vertices("Houston","Miami",968)

   city_graph2.add_edge_by_vertices("Atlanta","Chicago",588)
   city_graph2.add_edge_by_vertices("Atlanta","Washington",543)
   city_graph2.add_edge_by_vertices("Atlanta","Miami",604)

   city_graph2.add_edge_by_vertices("Miami","Washington",923)

   city_graph2.add_edge_by_vertices("Chicago","Detroit",238)

   city_graph2.add_edge_by_vertices("Detroit","Boston",613)
   city_graph2.add_edge_by_vertices("Detroit","Washington",396)
   city_graph2.add_edge_by_vertices("Detroit","New York",482)

   city_graph2.add_edge_by_vertices("Boston","New York",190)

   city_graph2.add_edge_by_vertices("New York","Philadelphia",81)

   city_graph2.add_edge_by_vertices("Philadelphia","Washington",123)
 
#%S
#  print("\n@@ All methods of class(WeightedGraph): <{a}>".format(a=dir(WeightedGraph)) )
#  X = dir(WeightedGraph)
#  for i in range(0,len(X)):
#      print("@@ All methods of class(WeightedGraph): [{a}], method: <{b}>".format(a=i,b=X[i]) )
#
#  object_methods = [method_name for method_name in dir(WeightedGraph)
#                    if callable(getattr(WeightedGraph, method_name))]
#  print("\n@@ Callable methods of class(WeightedGraph)")
#  for i in range(0,len(object_methods)):
#     print("  i: <{a}>, b: <{b}>".format(a=i,b=object_methods[i]) )
#
#  object_nc_methods = [method_name for method_name in dir(WeightedGraph)
#                    if not callable(getattr(WeightedGraph, method_name))]
#  print("\n@@ Non_callable methods of class(WeightedGraph): {a}".format(a=object_nc_methods) )
#
#%E
   print(city_graph2) # Depends of __str__ defined here
 
   print("=============")

# -- end of file
