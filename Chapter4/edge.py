# edge.py
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
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    u: int # the "from" vertex
    v: int # the "to" vertex

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"

if __name__ == "__main__":
   v1 = Edge(1,2)
   print("v1 should return '1 -> 2': <{a}>".format(a=v1) )
   print("v1.u should return '1' <{a}>, v1.v should return '2' <{b}>".format(
     a=v1.u,b=v1.v) )

   # Show a reversed v1
   v2 = v1.reversed()
   print("Reversed v1 (as v2) should be '2 -> 1' <{a}>".format(a=v2) )

   print("Original v1 should still be '1 -> 2' <{a}>".format(a=v1) )
   print("v2 is <{a}>".format(a=v2) )

# -- end of file
