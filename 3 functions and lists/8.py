#!/usr/bin/env python3

n = int(input())
m = int(input())


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

g = gcd(n, m)

print(n//g, m//g)