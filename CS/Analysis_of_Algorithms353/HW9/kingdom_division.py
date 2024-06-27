#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter, deque

#
# Complete the 'kingdomDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def kingdomDivision(n, roads):
    # Write your code here
    edges_dict = defaultdict(set)
    degree = Counter()

    for edge in roads:
        u, v = edge
        edges_dict[u].add(v)
        edges_dict[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # The possible divisions for a sub-tree rooted at node is
    # count[node][parent], where parent = True if the node shares its parent's color
    count = {u: {True: 1, False: 1} for u in degree}

    # We accumulate counts by iteratively stripping leaves from the tree
    leaves = deque([u for u in degree if degree[u] == 1])
    while True:
        node = leaves.popleft()

        # If parent differs, exclude case where ALL children differ
        count[node][False] = count[node][True] - count[node][False]

        # If no edges left, we have reached root and are done
        if not degree[node]:
            root = node
            break
        else:
            # Otherwise update parent:
            parent = edges_dict[node].pop()

            # Update topology
            edges_dict[parent].discard(node)
            degree[parent] -= 1
            if degree[parent] == 1:
                leaves.append(parent)

            # Update counts
            count[parent][True] *= count[node][True] + count[node][False]
            count[parent][False] *= count[node][False]

    # Note each division has a corresponding one with colors switched
    total = 2 * count[root][0]
    return total % (10**9 + 7)


result = kingdomDivision(5, [(1, 2), (1, 3), (3, 4), (3, 5)])
print(result)