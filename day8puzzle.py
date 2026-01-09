# --- Day 8: Playground ---
# 
# Summary:
# - Algorithm: Union-Find (Disjoint Set Union) for tracking connected components
# - Data Structures: List comprehensions, Counter for counting, tuples for coordinates
# - Patterns: itertools.combinations for pairwise operations, sorted() for ordering, zip() for distance
# - Math: 3D Euclidean distance calculation using sum of squared differences
#
# Approach: Calculate all pairwise distances using combinations and zip, sort by distance.
# Part 1: Connect 1000 shortest pairs, use Counter to count component sizes, multiply three largest.
# Part 2: Continue connecting pairs until all boxes are in one circuit, multiply X coordinates
# of the last connection that completes the single circuit.

import math
from collections import Counter
from itertools import combinations

class UnionFind:
    """Union-Find with path compression and union by rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

with open('day8input.txt', 'r') as f:
    points = [tuple(map(int, line.split(','))) for line in f.read().strip().split('\n')]

edges = sorted(
    (math.sqrt(sum((a - b)**2 for a, b in zip(points[i], points[j]))), i, j)
    for i, j in combinations(range(len(points)), 2)
)

uf1 = UnionFind(len(points))
for dist, i, j in edges[:1000]:
    uf1.union(i, j)

sizes = sorted(Counter(uf1.find(i) for i in range(len(points))).values(), reverse=True)
print("part 1: ", sizes[0] * sizes[1] * sizes[2])

uf2 = UnionFind(len(points))
components = len(points)

for dist, i, j in edges:
    if uf2.union(i, j):
        components -= 1
        if components == 1:
            print("part 2: ", points[i][0] * points[j][0])
            break
