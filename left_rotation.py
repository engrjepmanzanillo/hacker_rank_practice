#!/bin/python3
#author: @engrjepmanzanillo
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #nd = input().split()

    n = 5

    d = 4

    a = [1,2,3,4,5]

    diff = n - d
    b = a[:-diff]
    b = [str(x) for x in b]
    b = ' '.join(b)
    c = a[d:]
    c = [str(x) for x in c]
    c = ' '.join(c)
    print(c,b)
