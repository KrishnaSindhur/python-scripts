#!/bin/python3

import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Complete this function
    if y1>y2:
        return 10000
    elif y1 < y2:
        return 0
    elif m1 < m2 and y1 < y2:
        return 0
    elif d1>d2 and m1<m2:
        return 0
    elif m1>m2:
        return 500*(m1-m2)
    elif d1>d2:
        return 15*(d1-d2)
    else:
        return 0

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
