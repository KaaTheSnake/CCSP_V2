# dna_search.py
# From Classic Computer Science Problems in Python Chapter 2
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

# Listing L2.(1-X); File: dna_serach.py

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

#gene_str: str = "ACG_TGG_CTC_TCT_AAC_GTA_CGT_ACG_TAC_GGG_GTT_TAT_ATA_TAC_CCT_AGG_ACT_CCC_TTT"
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene

my_gene: Gene = string_to_gene(gene_str)

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:  # while there is still a search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

if __name__ == "__main__":
   acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
   gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
  #print(linear_contains(my_gene, acg))  # True

   # -- Linear search (may be unsorted)
   if linear_contains(my_gene, acg):
      print("The string <{a}> contains codon <{b}>".format(
        a=gene_str,b='acg') )
   else:
      print("The string <{a}> does NOT contain codon <{b}>".format(
        a=gene_str,b='acg') )

  #print(linear_contains(my_gene, gat))  # False
   if linear_contains(my_gene, gat):
      print("The string <{a}> does contains codon <{b}>".format(
        a=gene_str,b='gat') )
   else:
      print("The string <{a}> does NOT contain codon <{b}>".format(
        a=gene_str,b='gat') )

   # -- Binarysearch (must be sorted)
   my_sorted_gene: Gene = sorted(my_gene)

  #print(binary_contains(my_sorted_gene, acg))  # True
   if binary_contains(my_sorted_gene, acg):
      print("[BS] The sorted string <{a}> does contains codon <{b}>".format(
        a=my_sorted_gene,b='acg') )
   else:
      print("[BS] The sorted string <{a}> does NOT contain codon <{b}>".format(
        a=my_sorted_gene,b='acg') )

  #print(binary_contains(my_sorted_gene, gat))  # False
   if binary_contains(my_sorted_gene, gat):
      print("[BS] The sorted string <{a}> does contains codon <{b}>".format(
        a=my_sorted_gene,b='gat') )
   else:
      print("[BS] The sorted string <{a}> does NOT contain codon <{b}>".format(
        a=my_sorted_gene,b='gat') )

# -- end of file
