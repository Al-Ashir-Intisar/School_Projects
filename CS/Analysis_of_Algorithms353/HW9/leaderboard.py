#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
 
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    res = []
    positions = sorted(set(ranked))
    top = len(positions)
    for j in range(len(player)):
        place = bisect.bisect(positions, player[j])
        res.append(top - place + 1)
    return res

ranked = [100, 90, 90, 80]
player = [70, 80, 105]

result = climbingLeaderboard(ranked, player)

print(result)