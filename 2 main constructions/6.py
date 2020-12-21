#!/usr/bin/env python3

n = int(input())

x60 = n // 60
x10 = (n - x60 * 60) // 10
x1 = (n - x60 * 60 - x10 * 10)

if x1 * 15 + x10 * 125 > 440:
    x10 = x1 = 0
    x60 += 1

if x1 * 15 > 125:
    x1 = 0
    x10 += 1

if x10 * 125 > 440:
    x10 = 0
    x60 += 1

print(x1, x10, x60)
