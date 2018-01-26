#!/bin/python

import sys

def taumBday(b, w, x, y, z):
    a = 0
    a1 = 0
    if y+z < x:
        a = b * (y+z)
    else:
        a = b * x
    if x+z < y:
        a1 = w * (x+z)
    else:
        a1 = w * y
    ans = a + a1
    return ans
    #t -=  1

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        b, w = raw_input().strip().split(' ')
        b, w = [int(b), int(w)]
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = taumBday(b, w, x, y, z)
        print result
