#!/bin/python3
#author: @engrjepmanzanillo
import math
import os
import random
import re
import sys

def list_slicer(list):
    list = [str(x) for x in list]
    list = ' '.join(list)
    return list


if __name__ == '__main__':
    #nd = input().split()

    n = 5

    d = 4

    a = [1,2,3,4,5]

    b = list_slicer(a[:d-n])
    c = list_slicer(a[d:])
    print(c,b)
