#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    return ''.join(
        s[i].upper() if i == 0 or s[i-1].isspace()
        else s[i]
        for i in range(len(s))
    )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
