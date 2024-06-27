
import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    # Write your code here
    n = len(arr)
    plants = 0
    i = 0

    while i < n:
        found = False
        for j in range(min(i + k - 1, n - 1), max(-1, i - k), -1):
            if arr[j] == 1:
                plants += 1
                i = j + k
                found = True
                break

        if not found:
            return -1

    return plants

result = pylons(3, [0,1,1,1,0,0])
print(result)