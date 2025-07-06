#!/bin/python3

import math
import os
import random
import re
import sys

def myfunct(e):
     return -e[1],e[0]
if __name__ == '__main__':
    s = input()
    counted =[[i,s.count(i) ]for i in set(s)]
    counted.sort(key = myfunct)
    print('\n'.join(map(lambda x: f"{x[0]} {x[1]}",counted[:3])))
